from rest_framework import serializers
from Book.models import Publisher,Writer,Book
from Address.models import Address


class AddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = ['city','street']


class PublisherSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Publisher
        fields = ['id','name','phone','address']

    def get_address(self, obj):
        try:
            address = Address.objects.get_address_for(Publisher, obj.id)
            serializer = AddressSerializer(address,many=False)
            return serializer.data
        except:
            return 'no address'
        

class WriterSerializer(serializers.ModelSerializer):
        class Meta:
            model = Writer
            fields = ['id','first_name','last_name','surname'] 


class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ['id','title','pages','year_publication','writers','publisher'] 

        