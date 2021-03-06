# Generated by Django 3.0.2 on 2020-11-15 05:12

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]
 
    operations = [
        migrations.AddField(
            model_name='book',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='貸出期限'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isAvailable',
            field=models.BooleanField(default=True, verbose_name='貸出可否'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='purchaseDate',
            field=models.DateTimeField(auto_now_add=False, default=None, verbose_name='購入日'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30, verbose_name='著者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookid',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='本番号'),
        ),
        migrations.AlterField(
            model_name='book',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新日時'),
        ),
    ]
