from rest_framework import serializers

from lessons.models import Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    viewed_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('description', 'status', 'viewed_time')


class LessonsByProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    viewed_time = serializers.IntegerField()
    last_viewed_date = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('description', 'status', 'viewed_time', 'last_viewed_date')


class ProductStatisticSerializer(serializers.Serializer):
    prod_name = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_on_product = serializers.IntegerField()
    purchasing_percent = serializers.FloatField()
