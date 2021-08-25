from django.db import models

# Create your models here.
class Attend(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    subject = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
        