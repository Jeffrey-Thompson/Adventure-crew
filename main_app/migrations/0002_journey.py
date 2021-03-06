# Generated by Django 3.1.2 on 2020-10-05 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=100)),
                ('challenge', models.CharField(max_length=100)),
                ('reward', models.CharField(max_length=100)),
                ('adventurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.adventurer')),
            ],
        ),
    ]
