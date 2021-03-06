# Generated by Django 3.1 on 2020-10-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='business_number',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='call_number',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='food_origin',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='open_time',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
