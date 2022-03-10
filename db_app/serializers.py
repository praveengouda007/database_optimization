from rest_framework import serializers
from .models import *

class A_Serializer(serializers.ModelSerializer):
    c = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    b = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = A
        fields = ["name", "b", "c"]


class B_Serializer(serializers.ModelSerializer):

    class Meta:
        model = B
        fields = ["id", "name", "a"]

        depth=1


class C_Serializer(serializers.ModelSerializer):
    a = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = B
        fields = ["id", "name", "a"]