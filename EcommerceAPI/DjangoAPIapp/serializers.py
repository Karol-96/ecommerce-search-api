from rest_framework import serializers
from .models import Category,Books,Product


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


class BooksSerializer(serializers.ModelSerializer):


    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'sku',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'
        )
        model = Books

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created'
        )
        model =Product