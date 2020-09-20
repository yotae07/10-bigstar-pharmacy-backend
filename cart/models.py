from django.db import models

class Cart(models.Model):
    item      = models.CharField(max_length=100, null=True)
    count     = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    product   = models.ForeignKey("product.Product", on_delete=models.SET_NULL, null=True, related_name='cart_product')
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)
    user      = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'carts'
