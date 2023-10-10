from django.db.models import F, Q, FilteredRelation
from .serializers import LessonSerializer
from rest_framework import viewsets, permissions, mixins

from lessons.models import Lesson
from products.models import ProductAccess


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
