from django.db import models

# Create your models here.
class Persons(models.Model) :
    col = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 15, default="", editable=False)
    last_name = models.CharField(max_length = 15, default="", editable=False)
    s_id = models.CharField(max_length = 10, default="", editable=False)
