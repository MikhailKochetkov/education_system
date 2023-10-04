from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    description = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.PositiveIntegerField()


class LessonViewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    last_viewed_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.viewed_time < self.lesson.duration * 0.8:
            self.status = False
        else:
            self.status = True
        super().save(*args, **kwargs)
