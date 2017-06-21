from rest_framework import serializers
from laptops.models import Laptop, CPU


class LaptopSerializer(serializers.ModelSerializer):
    cpu = serializers.StringRelatedField()
    manufacturer = serializers.StringRelatedField()
    gpu = serializers.StringRelatedField(many=True)

    class Meta:
        model = Laptop
        fields = ('id', 'manufacturer', 'model_name', 'year', 'cpu', 'weight', 'ram', 'storage', 'battery', 'gpu')
