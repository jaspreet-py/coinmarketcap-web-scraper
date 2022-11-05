from django.shortcuts import render
from rest_framework import viewsets

from .models import Currency
from .serializers import CurrencySerializer


# Create your views here.
class IndexView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
