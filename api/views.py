from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from laptops.models import Laptop
from .serializers import LaptopSerializer


class LaptopsAll(APIView):

    def get_object(self):
        try:
            return Laptop.objects.all()
        except Laptop.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = self.get_object()
        serializer = LaptopSerializer(queryset, many=True)
        return Response(serializer.data)


class LaptopsFilter(APIView):

    def get_object(self):
        cpu = self.request.query_params.get('cpu', None)
        year = self.request.query_params.get('year', None)
        ram = self.request.query_params.get('ram', None)

        filterargs = {'year': year, 'ram': ram}

        return Laptop.objects.filter(year=year, ram=None)

    def get(self, request):
        queryset = self.get_object()
        serializer = LaptopSerializer(queryset, many=True)
        return Response(serializer.data)
