from django.db import models

# Create your models here.
class NiftyModel(models.Model):
    label = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    change = models.CharField(max_length=50)
    change_percent = models.CharField(max_length=50)
    volume_lacs = models.CharField(max_length=50)
    turnover_crs = models.CharField(max_length=50)

    class Meta:
        db_table = 'NiftyModel'