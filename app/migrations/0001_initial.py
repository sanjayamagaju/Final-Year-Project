# Generated by Django 4.0.2 on 2022-04-17 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuturePurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=None, max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images/')),
                ('desc', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=None, max_length=50)),
                ('donor', models.CharField(max_length=80)),
                ('donation_amt', models.IntegerField()),
                ('camp_detail', models.CharField(max_length=30)),
                ('date_donation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtherCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Target', models.IntegerField()),
                ('Collected', models.IntegerField(default=0)),
                ('Info', models.CharField(max_length=300)),
                ('Date_added', models.DateField(auto_now_add=True)),
                ('Amount', models.IntegerField(default=0, null=True)),
                ('Dontaion_count', models.IntegerField(default=0, null=True)),
                ('manager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
