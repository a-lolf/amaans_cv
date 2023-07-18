from rest_framework import serializers
from .models import ContactMe


class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = '__all__'

    # def to_internal_value(self, data):
    #     return super().to_internal_value(data)
