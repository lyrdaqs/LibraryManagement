from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from .models import *
from Address.models import Address
from .mixins import AdminRequiredMixin
from .forms import PublisherCreateForm
from django.urls import reverse


@login_required
def home(request):
    if request.user.is_staff == True:
        return render(request, 'book/index.html')
    else:
        return HttpResponse('<h2>you are not admin</h2>') 



class BookListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
    template_name = 'book/booklist.html'
    context_object_name = 'books'
    ordering = ['-year_publication']
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        book_filtered = Book.objects.get_book_list(query)
        print(book_filtered)  
        return book_filtered


class BookDetailView(LoginRequiredMixin,AdminRequiredMixin,DetailView):
    context_object_name = 'book'
    template_name = 'book/bookdetail.html'
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Book.objects.get_detail_book(pk)     
        return queryset
    

class BookCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
    model = Book
    template_name = 'book/bookcreate.html'
    fields = '__all__'


class BookUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
    model = Book
    template_name = 'book/bookupdate.html'
    fields = '__all__'


class BookDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = Book
    template_name = 'book/bookdelete.html'
    success_url = '/booklist'



class WriterListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
    model = Writer
    template_name = 'book/writerlist.html'
    context_object_name = 'writers'
    ordering = ['surname']
    paginate_by = 8


class WriterDetailView(LoginRequiredMixin,AdminRequiredMixin,DetailView):
    context_object_name = 'writer'
    template_name = 'book/writerdetail.html'
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Writer.objects.get_detial_writer(pk)       
        return queryset


class WriterCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
    model = Writer
    template_name = 'book/writercreate.html'
    fields = '__all__'


class WriterUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
    model = Writer
    template_name = 'book/writerupdate.html'
    fields = '__all__'


class WriterDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = Writer
    template_name = 'book/writerdelete.html'
    success_url = '/writerlist'


class PublisherListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
    model = Publisher
    template_name = 'book/publisherlist.html'
    context_object_name = 'publishers'
    ordering = ['name']
    paginate_by = 8


class PublisherDetailView(LoginRequiredMixin,AdminRequiredMixin,DetailView):
    context_object_name = 'publisher'
    template_name = 'book/publisherdetail.html'
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Publisher.objects.get_detial_publisher(pk)       
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['address'] = Address.objects.get_address_for(Publisher,pk)
        return context
    

class PublisherCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'book/publishercreate.html'

    def form_valid(self,form):
        form.create_publisher_with_address(self.request, Address)
        return super().form_valid(form)


class PublisherUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'book/publisherupdate.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        publisher = self.object
        address = Address.objects.get_address_for(Publisher,publisher.pk)
        form.fields['city'].initial = address.city
        form.fields['street'].initial = address.street
        return form

    def form_valid(self,form):
        form.update_publisher_with_address(self.request, Address)
        return super().form_valid(form)


class PublisherDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = Publisher
    template_name = 'book/publisherdelete.html'
    success_url = '/publisherlist'

    
