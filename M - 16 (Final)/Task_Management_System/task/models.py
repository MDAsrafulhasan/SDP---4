from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle  = models.CharField(max_length=100)
    taskDescription  = models.TextField(max_length=200)
    is_completed =models.BooleanField(default=False)
    Task_Assign_Date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.taskTitle
