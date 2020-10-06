# Generated by Django 3.1.2 on 2020-10-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_journey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('treasure', models.IntegerField()),
                ('health', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='adventurer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='adventurer',
            name='style',
            field=models.CharField(max_length=100, verbose_name='combat style'),
        ),
        migrations.AlterField(
            model_name='adventurer',
            name='weapon',
            field=models.CharField(max_length=100, verbose_name='perferred weapon'),
        ),
        migrations.AddField(
            model_name='adventurer',
            name='enemys',
            field=models.ManyToManyField(to='main_app.Enemy'),
        ),
    ]
