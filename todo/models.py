from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TodoList(models.Model):
    item = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all().first())
    date_created = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item


