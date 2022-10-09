from rest_framework import serializers

from expense.models import Outlay, Material, OutlayType


class OutlayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutlayType
        fields = [
            "id",
            "name",
            "description",
        ]


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            "id",
            "name",
            "is_service",
            "description",
        ]


class OutlaySerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    outlay_type = OutlayTypeSerializer()

    class Meta:
        model = Outlay
        fields = ['id', 'material', 'outlay_type', 'owner', 'price', 'date', 'description']
