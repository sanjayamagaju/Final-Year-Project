# Generated by Django 4.0.3 on 2022-04-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_khalti_remove_othercampaign_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='desc',
            field=models.CharField(default=None, max_length=50),
        ),
    ]