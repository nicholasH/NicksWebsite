from django.db import models

# Create your models here.
class businessCard(models.Model):
    email = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    biz_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


    def __str__(self):
        return self.contact_name

