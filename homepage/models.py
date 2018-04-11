from django.db import models

# Create your models here.
class homepage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    biz_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Message = models.CharField(max_length=255)


    def __str__(self):
        return self.title