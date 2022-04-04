from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Other camapigns
class OtherCampaign(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    Name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='images/')
    Target = models.IntegerField()
    Collected = models.IntegerField()
    Info = models.CharField(max_length=300)
    Date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-id']

# gallery
class Gallery(models.Model):
    Image = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.Image


# khalti payment
class Khalti(models.Model):
    campaign_name = models.CharField(max_length=30)
    amount = models.IntegerField()
    # token = models.CharField(max_length=30)


    def __str__(self):
        return self.campaign_name
    