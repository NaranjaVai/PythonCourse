from django.urls import path
from .views import index, insertData, search

urlpatterns = [
    path('', index, name='index'),
    path('insertData/', insertData, name='InsertData'),
    path('search/', search, name='search')
]