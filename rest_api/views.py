from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer, StockSerializerCreate

# Create your views here.

class StockList(APIView):

    # spd - display stock
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer( stocks, many=True) # specify objects that would be serializer and many of them or not
        return Response(serializer.data)

    # spd - create new stock
    def post(self, request, format=None):
        serializer = StockSerializerCreate( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
