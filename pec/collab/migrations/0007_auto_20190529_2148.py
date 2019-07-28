# Generated by Django 2.2.1 on 2019-05-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0006_carpenter_dist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carpenter',
            options={'ordering': ['dist']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='Services',
            field=models.TextField(blank=True, null=True),
        ),
    ]
