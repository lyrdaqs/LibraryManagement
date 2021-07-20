from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class AddressManager(models.Manager):
    def get_address_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        address = Address.objects.filter(
            content_type=content_type,
            object_id=obj_id
        )
        if address:
            return address[0]
        return Address(city='',street='')
 
    def create_address_for(self, city, street, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        address = Address(
            city=city,
            street=street,
            content_type=content_type,
            object_id=obj_id
        )
        address.save()


class Address(models.Model):
    objects = AddressManager()
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType,
        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together   = ('content_type', 'object_id')

