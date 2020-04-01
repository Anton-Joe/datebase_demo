
from django.urls import path
from . import views
app_name = 'db_app1'
urlpatterns = [
    path('', views.index),
]
