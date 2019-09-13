from django.db import models
from tinymce.models import HTMLField
# from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)

class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='df_goods')
    gprice=models.DecimalField(max_digits=3,decimal_places=2,)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20)
    gclick=models.IntegerField()
    gintroduction=models.CharField(max_length=200)
    gstock=models.IntegerField()
    gcontent=HTMLField()
    gtype=models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    gadv=models.IntegerField()
# class