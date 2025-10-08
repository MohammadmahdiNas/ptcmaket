from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..models import Apply, Contact, Order
from .serializers import ApplySerializer, ContactSerializer, OrderSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class ApplyViewSet(ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

