# Generated by Django 3.2.9 on 2021-11-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonBooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
