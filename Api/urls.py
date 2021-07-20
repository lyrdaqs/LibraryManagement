from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('publishers/', publisher_list, name='publishers'),
    path('writers/', writer_list, name='writers'),
    path('<int:pk>/publisher_books/', get_publisher_books, name='publisher_books'),
    path('<int:pk>/writer_books/', get_writer_books, name='writer_books'),
    path('<int:pk>/add_book/', add_book_for_writer, name='add_book'),
]