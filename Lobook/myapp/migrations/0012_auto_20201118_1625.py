# Generated by Django 3.0.2 on 2020-11-18 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20201118_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='Id',
        ),
        migrations.AddField(
            model_name='login',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
            preserve_default=False,
        ),
    ]