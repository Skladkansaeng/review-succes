from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models import Avg, Count


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    score = models.SmallIntegerField(default=0)
    review = models.CharField(max_length=255, default='')

    @staticmethod
    def is_user_exists(user):
        return Review.objects.filter(user=user).exists()

    @staticmethod
    def get_average():
        return Review.objects.aggregate(Avg('score'))

    @staticmethod
    def get_frequency():
        return Review.objects.values('score').annotate(count=Count('score'))
