from django.db import models
import datetime
from partial_date import PartialDateField
from django.urls import reverse


class WriterManager(models.Manager):
    def get_detial_writer(self, pk):
        detail_obj = Writer.objects.prefetch_related('book_set').filter(pk=pk)  
        return detail_obj


class PublisherManager(models.Manager):
    def get_detial_publisher(self, pk):
        detail_obj = Publisher.objects.prefetch_related('book_set').filter(pk=pk)  
        return detail_obj


class BookManager(models.Manager):
    def get_book_list(self, query):
        if query == None:
            query = ''
            return Book.objects.select_related('publisher').all()
        book_filtered = Book.objects.select_related('publisher')\
            .filter(title__icontains=query)
        return book_filtered

    def get_detail_book(self,pk):
        return Book.objects.select_related('publisher')\
        .prefetch_related('writers').filter(pk=pk)


class Writer(models.Model):
    objects = WriterManager()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('book:writerdetail',kwargs={'pk':self.pk})
    

class Publisher(models.Model):
    objects = PublisherManager()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:publisherdetail',kwargs={'pk':self.pk})


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    year_publication = PartialDateField()
    writers = models.ManyToManyField(Writer)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:bookdetail',kwargs={'pk':self.pk})



