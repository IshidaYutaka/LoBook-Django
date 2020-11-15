from django.db import models
from django.utils import timezone
# bookid: int
# title:タイトル　char
# auther:著者名 char
# updatedAt:更新日時 date
# createdAt:作成日時 date
# purchaseDate:購入日 date
# deadline:貸し出し期限 date
# isAvailable:貸し出し状態 bool


class Book(models.Model):   
    bookid = models.IntegerField('本番号',primary_key=True)
    title = models.CharField('タイトル',max_length=100)
    author = models.CharField('著者',max_length=30)
    updatedAt = models.DateTimeField('更新日時',default=timezone.now)
    createdAt = models.DateTimeField('作成日',default=timezone.now)
    purchaseDate = models.CharField('購入日' ,max_length=30)
    deadline = models.DateField('貸出期限',auto_now_add=True)
    producedby = models.CharField('出版社',max_length=30)
    isAvailable = models.BooleanField('貸出可否')

    def __str__(self):
        return '<id:'+ self.bookid + ',' + self.title + ',' + self.author + '>'


