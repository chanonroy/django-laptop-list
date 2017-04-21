from django.shortcuts import render
from .models import Laptop


def index(request):
    """ Brings up the home page """

    laptops = Laptop.objects.all()

    context_dict = {
        'laptops': laptops
    }

    print(laptops)

    return render(request, 'laptops/index.html', context=context_dict)
