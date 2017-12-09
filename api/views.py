from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from laptops.models import Laptop
from .serializers import LaptopSerializer


def gather_arguments(request, params):
    """ Build list of filtering parameters """
    args = {}
    for param in params:
        value = request.query_params.get(param, None)
        if value is not None:
            args[param] = value
    return args

class Laptops(APIView):

    def get_object(self):
        filter_params = ['cpu', 'year', 'ram']
        filter_args = gather_arguments(self.request, filter_params)

        return Laptop.objects.filter(**filter_args)

    def get(self, request):
        queryset = self.get_object()
        serializer = LaptopSerializer(queryset, many=True)
        return Response(serializer.data)