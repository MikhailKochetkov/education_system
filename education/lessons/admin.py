from django.contrib import admin
from .models import Lesson, LessonView


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'description',
        'video_link',
        'duration',
    )
    empty_value_display = '-пусто-'


class LessonViewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'lesson',
        'viewed_time',
        'status',
        'last_viewed_date',
    )
    search_fields = ('user', 'lesson',)
    list_filter = ('lesson',)
    empty_value_display = '-пусто-'


admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonView, LessonViewAdmin)
