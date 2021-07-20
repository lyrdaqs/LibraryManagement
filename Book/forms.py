from django import forms
from .models import Publisher
from django.forms import ModelForm

class PublisherCreateForm(ModelForm):
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)

    class Meta:
        model = Publisher
        fields = ['name','phone','city','street']

    def create_publisher_with_address(self, request, Address):
        publisher = self.save()
        city = request.POST.get('city')
        street = request.POST.get('street')
        Address.objects.create_address_for(city,street,
            Publisher, publisher.id)
   
    def update_publisher_with_address(self, request, Address):
        publisher = self.save()
        city = request.POST.get('city')
        street = request.POST.get('street')
        address = Address.objects.get_address_for(Publisher, publisher.id)
        if address.id:
            address.city =city
            address.street=street
            address.save()
        else:
            Address.objects.create_address_for(city,street,
                Publisher, publisher.id)



