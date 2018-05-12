from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=128)
    deadline = models.DateField()
    progress = models.SmallIntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(100)])
    done = models.BooleanField()
