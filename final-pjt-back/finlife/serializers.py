from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Bank


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='DepositOptions.product')
    class Meta:
        model = DepositOptions
        # read_only_fields = ('product',)
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='SavingOptions.product')
    class Meta:
        model = SavingOptions
        # read_only_fields = ('product',)
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
