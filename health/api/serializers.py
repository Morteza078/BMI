from rest_framework import serializers


class BMISerializer(serializers.Serializer):
    weight = serializers.FloatField()
    height = serializers.FloatField()

    class Meta:
        fields = ['weight', 'height']
