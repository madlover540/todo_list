from cProfile import label
from django.db import models

# Create your models here.


class TodoListModel(models.Model):
    task = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    class Meta:
        ordering = ['-date']