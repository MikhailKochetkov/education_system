from django.contrib import admin
from .models import Lesson, LessonView


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'get_products',
        'description',
        'video_link',
        'duration',
    )
    search_fields = ('get_products',)
    empty_value_display = '-пусто-'

    def get_products(self, obj):
        return "\n".join([p.products for p in obj.product.all()])


class LessonViewerAdmin(admin.ModelAdmin):
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
admin.site.register(LessonView, LessonViewerAdmin)
