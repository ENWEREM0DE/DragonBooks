# Generated by Django 3.2.9 on 2022-01-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonBooks', '0004_rename_title_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
