# Generated by Django 2.2.2 on 2019-10-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_baset_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='baset',
            name='path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
