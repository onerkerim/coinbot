from django.db import models

# Create your models here.
class api_keys(models.Model):
    id      = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    api_key     = models.CharField(max_length=200)
    api_secret_key = models.CharField(max_length=200)
