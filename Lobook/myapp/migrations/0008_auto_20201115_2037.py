# Generated by Django 3.0.2 on 2020-11-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201115_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新日時'),
        ),
    ]
