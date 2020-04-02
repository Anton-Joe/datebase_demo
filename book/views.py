from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.


def index(request):
    # # 1. 使用ORM添加一条数据到数据库中
    # book = Book(name='三国演义2', author='YJX68', price=200)
    # book.save()

    # # 2. 查询数据
    # # 2.1 根据主键方式进行查找
    # book = Book.objects.get(pk=2)
    # # 2.2 根据其他字段查找
    # book = Book.objects.filter(name='三国演义').first()

    # # 3. 删除数据
    # book = Book.objects.get(pk=2)
    # book.delete()

    # 4. 修改数据
    book = Book.objects.get(pk=2)
    book.price = 1600
    book.save()
    return HttpResponse(book)






