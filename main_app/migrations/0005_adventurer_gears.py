# Generated by Django 3.1.2 on 2020-10-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_gear'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurer',
            name='gears',
            field=models.ManyToManyField(to='main_app.Gear'),
        ),
    ]
