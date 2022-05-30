from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from resto.models import Contact
from resto.serializers import ContactSerializer


class ContactAPIViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
