from rest_framework import serializers
from laptops.models import Laptop


class LaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laptop
        fields = ('model_name', 'year')
        # fields = '__all__'
