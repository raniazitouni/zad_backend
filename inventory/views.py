from django.shortcuts import render
from django.http import JsonResponse
from models import Product
from serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#views here 

