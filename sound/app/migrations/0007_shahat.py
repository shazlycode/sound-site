# Generated by Django 2.2.2 on 2019-10-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_husary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shahat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(default='محمود الشحات محمد انور', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
    ]