# Generated by Django 2.2.1 on 2019-05-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0003_auto_20190523_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpenter',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carpenter',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
