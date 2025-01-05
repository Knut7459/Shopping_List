from django.conf import settings
from django.db import models
from datetime import date

# Create your models here.
class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    created_from = models.CharField(max_length=100)
    P_Name = models.CharField(max_length=200)
    P_Gruppe = models.CharField(max_length=50)
    P_ID = models.CharField(max_length=12)
    done = models.BooleanField(default=False)

    def erledigt(self):
        self.done = True
        self.save()
        
    def loeschen(self):
        self.delete()

    def __str__(self):
        return str(self.id) + ' ' + self.P_ID + ' ' + self.P_Name