# Generated by Django 2.2.6 on 2019-12-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20191205_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='todos_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]