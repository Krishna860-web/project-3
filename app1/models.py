from django.db import models

class tbl_book(models.Model):
    

    bookname=models.CharField(max_length=100)
    author=models.CharField(max_length=80)
    price=models.IntegerField
    journel=models.CharField(max_length=100)
    class Meta:
       db_table="tbl_book"   

   
