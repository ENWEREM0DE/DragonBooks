# Generated by Django 3.2.9 on 2022-01-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dragonBooks', '0003_auto_20220121_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='name',
        ),
    ]
