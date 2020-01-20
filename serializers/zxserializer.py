from rest_framework import serializers

from zx.models import Equ, ZhuanLine, Equipment, Eapi, LineOfBusinessOutlets


class EquSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equ
        fields = '__all__'


class ZXSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZhuanLine
        fields = '__all__'


class EquipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class EaipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eapi
        fields = '__all__'


class LineOfBusinessOutletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineOfBusinessOutlets
        fields = '__all__'
