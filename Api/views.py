from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Book.models import Publisher,Writer,Book
from .serializers import (
    PublisherSerializer,
    WriterSerializer,
    BookSerializer
)


@api_view(['GET'])
def publisher_list(request):
    publishers = Publisher.objects.all()
    serializer = PublisherSerializer(publishers,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def writer_list(request):
    writers = Writer.objects.all()
    serializer = WriterSerializer(writers,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_publisher_books(request,pk):
    publisher = Publisher.objects.get(pk=pk)
    books = Book.objects.filter(publisher=publisher)
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_writer_books(request,pk):
    writer = Writer.objects.get(pk=pk)
    books = Book.objects.filter(writers__id=writer.id)
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_book_for_writer(request,pk):
    data = request.data
    book = Book.objects.create(
        title = data['title'],
        pages = data['pages'],
        year_publication = data['year_publication'],
        publisher_id = data['publisher_id'],
    )
    writer = Writer.objects.get(pk=pk)
    writer.book_set.add(book)
    serializer = BookSerializer(book,many=False)
    return Response(serializer.data)
