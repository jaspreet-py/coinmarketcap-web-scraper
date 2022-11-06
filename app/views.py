from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Currency
from .serializers import CurrencySerializer


# Create your views here.
class IndexView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return [Currency.objects.last()]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
