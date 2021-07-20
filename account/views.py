from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from .models import User
from Address.models import Address
from Book.mixins import AdminRequiredMixin
from .forms import UserCreateForm
from django.contrib.auth.views import LoginView



class LoginUserView(LoginView):
    template_name = 'account/login.html'


class UserListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
    queryset = User.objects.all()
    template_name = 'account/userlist.html'
    context_object_name = 'users'
    ordering = ['username']
    paginate_by = 8


class UserDetailView(LoginRequiredMixin,AdminRequiredMixin,DetailView):
    context_object_name = 'userobj'
    template_name = 'account/userdetail.html'
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = User.objects.filter(pk=pk)    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['address'] = Address.objects.get_address_for(User,pk)
        return context


class UserCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'account/usercreate.html'

    def form_valid(self,form):
        form.create_user_with_address(self.request, Address)
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'account/userupdate.html'
    context_object_name = 'userobj'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.object
        address = Address.objects.get_address_for(User,user.pk)
        form.fields['city'].initial = address.city
        form.fields['street'].initial = address.street
        return form

    def form_valid(self,form):
        form.update_user_with_address(self.request, Address)
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = User
    template_name = 'account/userdelete.html'
    success_url = '/account/userlist'