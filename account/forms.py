from django import forms
from .models import User
from django.forms import ModelForm

class UserCreateForm(ModelForm):
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username','first_name','last_name',
            'email','phone','date_birth','membership','city','street']

    def create_user_with_address(self, request, Address):
        user = self.save()
        city = request.POST.get('city')
        street = request.POST.get('street')
        Address.objects.create_address_for(city,street,
            User, user.id)
   
    def update_user_with_address(self, request, Address):
        user = self.save()
        city = request.POST.get('city')
        street = request.POST.get('street')
        address = Address.objects.get_address_for(User, user.id)
        if address.id:
            address.city =city
            address.street=street
            address.save()
        else:
            Address.objects.create_address_for(city,street,
                User, user.id)




