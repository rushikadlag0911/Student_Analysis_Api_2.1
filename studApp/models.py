from django.db import models

# Create your models here.
class studdetails(models.Model):

    name = models.CharField(max_length=55)
    roll_num = models.IntegerField(primary_key=True)
    DOB = models.DateField()

class studmarks(models.Model):

    roll_num = models.ForeignKey(studdetails, on_delete=models.CASCADE)
    English = models.IntegerField()
    Maths = models.IntegerField()
    History = models.IntegerField()
 