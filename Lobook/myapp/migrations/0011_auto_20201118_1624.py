# Generated by Django 3.0.2 on 2020-11-18 07:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AddField(
            model_name='login',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
            preserve_default=False,
        ),
    ]