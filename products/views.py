from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Coupon
from .serializers import productserializer, couponserializer
from rest_framework import status
from django.http import Http404

class productDetailes(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset) 
        serializer = productserializer(queryset, many=True)
        print(serializer.data)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = productserializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    


    




