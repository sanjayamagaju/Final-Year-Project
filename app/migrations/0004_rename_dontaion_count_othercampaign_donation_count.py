# Generated by Django 4.0.2 on 2022-04-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_othercampaign_amount_othercampaign_dontaion_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='othercampaign',
            old_name='Dontaion_count',
            new_name='Donation_count',
        ),
    ]