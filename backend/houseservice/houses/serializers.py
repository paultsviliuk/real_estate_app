from rest_framework import serializers

from .models import House


class HouseSerializer(serializers.ModelSerializer):
    """
    Serializer for the House model.
    """
    class Meta:
        """
        Meta class for HouseSerializer.
        Specifies the model and fields to include in the serialization.
        """
        model = House
        fields = '__all__'
