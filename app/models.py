from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import get

# Create your models here.

# Other camapigns
class OtherCampaign(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    Name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='images/')
    Target = models.IntegerField()
    Collected = models.IntegerField(default=0)
    Info = models.CharField(max_length=300)
    Date_added = models.DateField(auto_now_add=True)

    Amount = models.IntegerField(default=0)
    Donation_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-id']

# gallery
class Gallery(models.Model):
    Image = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.desc


# khalti payment future purpose 
class FuturePurpose(models.Model):
    token = models.CharField(max_length=50, default=None)
    amount = models.IntegerField()

    def __str__(self):
        return self.token

# leaderboard
class LeaderBoard(models.Model):
    token = models.CharField(max_length=50, default=None)
    donor = models.CharField(max_length=80)
    donation_amt = models.IntegerField()
    camp_detail = models.CharField(max_length=30)
    date_donation = models.CharField(max_length=100)

    def __str__(self):
        return self.token