from django.db import models

# Create your models here.
class PracticeModels(models.Model):
    # name = models.CharField(max_length=200)
    # email = models.EmailField(max_length=200)
    # model_choice = models.TextField()
    # title = models.CharField(max_length = 200)
    # description = models.TextField()
    # auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    # file_path_field = models.FilePathField(path='/path/to/files/')
    # generic_ip_address_field = models.GenericIPAddressField()
    # image_field = models.ImageField(upload_to='images/')
    # many_to_many_field = models.ManyToManyField(OtherModel)
    positive_big_integer_field = models.PositiveBigIntegerField()
    slug_field = models.SlugField()
    time_field = models.TimeField()