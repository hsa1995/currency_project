from rest_framework import serializers
from .models import CurrencyRate,Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model =Currency
        fields = [
            'id',
            'name',
            'abbreviation'
        ]

class CurrencyRateSerializer(serializers.ModelSerializer):
    currency1=CurrencySerializer()
    currency2 = CurrencySerializer()
    class Meta:
        model =CurrencyRate
        fields = [
            'id',
            'currency1',
            'currency2',
            'rate',
            'date',
        ]
