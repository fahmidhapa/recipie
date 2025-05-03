from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class add_tbl(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    ingrediants = models.CharField(max_length=30)
    image=models.FileField(upload_to='pic')
    instructions=models.CharField(max_length=200)


    

   
    