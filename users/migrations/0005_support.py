# Generated by Django 5.1.1 on 2025-04-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_coaches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField(max_length=64, verbose_name='Почта')),
                ('text', models.TextField(verbose_name='Текст сообщения  ')),
            ],
        ),
    ]
