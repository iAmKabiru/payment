# Generated by Django 2.2.4 on 2019-10-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191007_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
