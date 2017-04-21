from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from laptops.models import Laptop
from .serializers import LaptopSerializer


class LaptopList(APIView):

    def get(self, request):
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return Response(serializer.data)
