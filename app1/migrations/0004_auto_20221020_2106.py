# Generated by Django 3.1.3 on 2022-10-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_dress_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='pic',
            field=models.ImageField(default='', upload_to='app1/images'),
        ),
    ]
