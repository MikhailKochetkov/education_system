from django.db.models import F, Q, FilteredRelation, Count, OuterRef, Sum
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins, exceptions

from .serializers import LessonSerializer, LessonsByProductSerializer, ProductStatisticSerializer
from lessons.models import Lesson, LessonView
from products.models import ProductAccess, Product


class LessonViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        accessible_products = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        queryset = Lesson.objects.filter(
            products__in=accessible_products.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            viewed_time=F('view_info__viewed_time')
        )
        return queryset


class LessonsByProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = LessonsByProductSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        accessible_products = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        if not (product_id in accessible_products.values_list('product_id', flat=True)):
            raise exceptions.NotFound
        queryset = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            viewed_time=F('view_info__viewed_time'),
            last_viewed_date=F('view_info__last_viewed_date')
        )
        return queryset


class ProductStatisticViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )

    def get_queryset(self):
        total_users_count = User.objects.filter(is_active=True).count()
        queryset = Product.objects.all().annotate(
            lesson_view_count=Count(
                LessonView.objects.filter(
                    lesson__products=OuterRef('id'),
                    status=True
                ).values('id')
            ),
            total_view_time=Sum(
                LessonView.objects.filter(
                    lesson__products=OuterRef('id')
                ).values('viewed_time')
            ),
            total_users_on_product=Count(
                ProductAccess.objects.filter(
                    product_id=OuterRef('id')
                ).values('id')
            ),
            purchasing_percent=F('total_users_on_product') / float(total_users_count) * 100
        )
        return queryset
