# Generated by Django 2.2.3 on 2019-10-05 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_auto_20190903_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledge',
            name='id',
        ),
        migrations.AddField(
            model_name='knowledge',
            name='number',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='knowledge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.Knowledge'),
        ),
    ]
