from rest_framework import serializers

from lessons.models import Lesson, LessonView


class LessonViewSerializer(serializers.ModelSerializer):

    class Meta:
        models = LessonView
        fields = ('status', 'viewed_time', )


class LessonSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    viewed_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('description', 'status', 'viewed_time')
