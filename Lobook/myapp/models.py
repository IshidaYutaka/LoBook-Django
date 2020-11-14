from django.db import models

# bookid: int
# title:タイトル　char
# auther:著者名 char
# updatedAt:更新日時 date
# createdAt:作成日時 date
# purchaseDate:購入日 date
# deadline:貸し出し期限 date
# isAvailable:貸し出し状態 bool


class Book(models.Model):   
    bookid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    purchaseDate = models.DateField
    deadline = models.DateField
    isAvailable = models.BooleanField

    def all(self):
        return self


