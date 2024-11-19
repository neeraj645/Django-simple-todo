from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField()

    def __str__(self) -> str:
        return self.todo_name