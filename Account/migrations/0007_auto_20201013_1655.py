# Generated by Django 3.1 on 2020-10-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20201013_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='env_point',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
    ]
