# Generated by Django 4.0.3 on 2022-03-20 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_khalti_payment_khalti'),
    ]

    operations = [
        migrations.RenameField(
            model_name='khalti',
            old_name='amt',
            new_name='amount',
        ),
    ]
