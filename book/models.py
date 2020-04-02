from django.db import models

# Create your models here.

class Book(models.Model):
    # 1. id：int类型，自增长,AutoField表示自动增长，并且为int类型
    id = models.AutoField(primary_key=True)
    # 2. name: varchar类型，最长100，图书的名字
    name = models.CharField(max_length=100, null=False)
    # 3. author：varchar类型，最长100，图书的作者
    author = models.CharField(max_length=100, null=False)
    # 4. price: float类型，图书的价格
    price = models.FloatField(null=False, default=0)

    def __str__(self):
        # 重写类默认打印方法
        return "<Book:({name},{author},{price})>".format(name=self.name, author=self.author, price=self.price)
