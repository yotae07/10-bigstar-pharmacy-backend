from django.db import models

class User(models.Model):
    name          = models.CharField(max_length = 50)
    email         = models.EmailField(max_length = 100)
    contact       = models.CharField(max_length = 50)
    password      = models.CharField(max_length = 100)
    created_at    = models.DateTimeField(auto_now_add = True)
    update_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
