from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    last_updated_at = models.DateTimeField(default=timezone.now)
    quote = models.CharField(max_length=255)


    def __str__(self):
        return 'Trump Quote'