# Generated by Django 2.2.2 on 2019-10-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_shahat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(default='محمود علي البنا', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Shahat',
        ),
    ]
