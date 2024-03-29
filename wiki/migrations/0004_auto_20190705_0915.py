# Generated by Django 2.2.3 on 2019-07-05 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20190705_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.AddField(
            model_name='view',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.ViewType'),
        ),
    ]
