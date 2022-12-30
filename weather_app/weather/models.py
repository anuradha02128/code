from django.db import models

class Weather(models.Model):

   date  = models.CharField(max_length = 10)
   max_temp = models.CharField(max_length = 50,blank=True)
   min_temp = models.CharField(max_length = 50, blank=True)
   amt_precipitation = models.IntegerField(blank=True, null=True)
   year=models.CharField(max_length = 4, blank=True, null=True)

   class Meta:
      db_table = "weather"
      unique_together = ('date', 'max_temp','min_temp','amt_precipitation')

   def __str__(self):
        return self.pk



class Yield(models.Model):

   year  = models.CharField(max_length = 4)
   tot_harvested = models.IntegerField()

   class Meta:
      db_table = "yield"
