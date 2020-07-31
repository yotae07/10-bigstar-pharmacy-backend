from django.db import models

class Review(models.Model):
    name           = models.CharField(max_length=20)
    purchased_item = models.CharField(max_length=50)
    purchased_date = models.CharField(max_length=50)
    photo          = models.CharField(max_length=200)
    comment        = models.TextField()

    class Meta:
        db_table = 'reviews'
