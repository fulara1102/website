# Generated by Django 4.1 on 2022-08-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEbN6-Gy6xenhzrJmZkQHarZEt40XL_PJu4w&usqp=CAU', max_length=500),
        ),
    ]
