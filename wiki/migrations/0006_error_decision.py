# Generated by Django 2.2.3 on 2019-07-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='decision',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Решение'),
        ),
    ]
