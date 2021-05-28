from django.db import models
from user.models import User
from task_managment import settings

# Create your models here.


class Task(models.Model):
    class Task_Status(models.IntegerChoices):
        PENDING = 10, "PENDING"
        PROGRESS = 20, "IN PROGRESS"
        COMPLETED = 30, "COMPLETED",
        FAILED = 40, "FAILED"

    name = models.CharField(max_length=200)
    status = models.IntegerField(
        default=Task_Status.PENDING, choices=Task_Status.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
