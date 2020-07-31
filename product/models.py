from django.db import models


class Product(models.Model):
    item          = models.CharField(max_length=200)
    decoration    = models.CharField(max_length=200)
    icon1         = models.CharField(max_length = 50)
    icon2         = models.CharField(max_length = 50)
    description1  = models.CharField(max_length = 200)
    description2  = models.CharField(max_length = 200)
    description3  = models.CharField(max_length = 200)
    period        = models.CharField(max_length = 50)
    price         = models.CharField(max_length = 100)
    price_number  = models.IntegerField(null=True)
    colors        = models.CharField(max_length = 50, null=True)
    image_product = models.CharField(max_length = 100)

    class Meta:
        db_table = 'products'

class Product_detail(models.Model):
    icon1        = models.CharField(max_length = 50)
    icon2        = models.CharField(max_length = 50)
    explanation  = models.TextField()
    period       = models.CharField(max_length = 50)
    price        = models.CharField(max_length = 100)
    product      = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    image_detail = models.CharField(max_length = 100)
    rest         = models.TextField(null=True)

    class Meta:
        db_table = 'product_details'
