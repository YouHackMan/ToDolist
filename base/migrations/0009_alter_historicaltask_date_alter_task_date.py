# Generated by Django 4.2.6 on 2023-11-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_historicaltask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltask',
            name='date',
            field=models.DateField(default='2023-11-24'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-11-24'),
        ),
    ]
