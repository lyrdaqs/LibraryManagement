from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('B','Bronze'),
        ('D','Gold'),
        ('S','Silver'),
    ]
    phone = models.CharField(max_length=200)
    date_birth = models.DateField(blank=True, null=True)
    membership = models.CharField(max_length=1, 
        choices=MEMBERSHIP_CHOICES, default='B')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('account:userdetail',kwargs={'pk':self.pk})


