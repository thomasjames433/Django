from rest_framework import serializers
from .models import Student

class Stuser(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields=(
            'name','age'
        )