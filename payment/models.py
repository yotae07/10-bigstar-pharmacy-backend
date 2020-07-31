from django.db import models

class Payment(models.Model):
    name             = models.CharField(max_length=100)
    contact          = models.CharField(max_length=20)
    post_number      = models.CharField(max_length=10, null=True)
    address_street   = models.CharField(max_length=200)
    address_detail   = models.CharField(max_length=200)
    customer_request = models.TextField()
    points           = models.IntegerField()
    card_number      = models.CharField(max_length=30)
    expired_month    = models.IntegerField()
    expired_year     = models.IntegerField()
    birth            = models.IntegerField()
    card_kakao       = models.CharField(max_length=20, null=True)
    card_password    = models.IntegerField()
    product          = models.ForeignKey('task.Product', on_delete=models.SET_NULL, null=True)
    timestamp        = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated          = models.DateTimeField(auto_now_add=False, auto_now=True)
    user             = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    purchased_item   = models.CharField(max_length=100, null=True)
    price            = models.CharField(max_length=100, null=True)
    count            = models.CharField(max_length=100, null=True)
    total_price      = models.CharField(max_length=100, null=True)
    back_image       = models.CharField(max_length=200, null=True)
    pill_image       = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'payments'

