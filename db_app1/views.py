from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    SQL = 'SHOW DATABASES;'
    cursor.execute(SQL)
    result = cursor.fetchall()
    context = {
        'data': result
    }
    return render(request, 'db_app1_index.html', context=context)