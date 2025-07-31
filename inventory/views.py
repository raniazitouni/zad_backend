from django.shortcuts import render
from django.http import JsonResponse
from inventory.models import Product
from inventory.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


#views here 

class Products(APIView):

   def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   


class AddProduct(APIView):
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request, *args, **kwargs):
                  serializer_product = ProductSerializer(data=request.data)
                  if serializer_product.is_valid() : 
                      serializer_product.save()
                      return Response({'message': 'Object created successfully'}, status=status.HTTP_201_CREATED)
                  else:
                        # Return errors for product serializer
                        return Response({'errors': {'product': serializer_product.errors}}, status=status.HTTP_400_BAD_REQUEST)
         
class DeleteProduct(APIView):
    def delete(self, request, product_id, *args, **kwargs):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateProduct(APIView):
    def put(self, request, product_id, *args, **kwargs):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)