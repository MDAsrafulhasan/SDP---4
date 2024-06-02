from django.db import models
# Create your models here.

class CategoryModel(models.Model):
    Category_Name = models.CharField(max_length=50)
    # task = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.Category_Name
