# Generated by Django 5.1.1 on 2025-04-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0005_coaches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
    ]
