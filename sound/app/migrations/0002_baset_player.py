# Generated by Django 2.2.2 on 2019-10-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baset',
            name='player',
            field=models.CharField(default='', max_length=100),
        ),
    ]
