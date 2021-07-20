from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('', home, name='home'),
    path('booklist/', BookListView.as_view(), name='booklist'),
    path('writerlist/', WriterListView.as_view(), name='writerlist'),
    path('publisherlist/', PublisherListView.as_view(), name='publisherlist'),
    path('book/<int:pk>', BookDetailView.as_view() , name='bookdetail'),
    path('publisher/<int:pk>', PublisherDetailView.as_view() , name='publisherdetail'),
    path('writer/<int:pk>', WriterDetailView.as_view() , name='writerdetail'),
    path('book/create', BookCreateView.as_view() , name='bookcreate'),
    path('book/<int:pk>/update', BookUpdateView.as_view() , name='bookupdate'),
    path('book/<int:pk>/delete', BookDeleteView.as_view() , name='bookdelete'),
    path('writer/create', WriterCreateView.as_view() , name='writercreate'),
    path('writer/<int:pk>/update', WriterUpdateView.as_view() , name='writerupdate'),
    path('writer/<int:pk>/delete', WriterDeleteView.as_view() , name='writerdelete'),
    path('publisher/create', PublisherCreateView.as_view() , name='publishercreate'),
    path('publisher/<int:pk>/update', PublisherUpdateView.as_view() , name='publisherupdate'),
    path('publisher/<int:pk>/delete', PublisherDeleteView.as_view() , name='publisherdelete'),
]