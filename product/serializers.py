from rest_framework import serializers


from product.models import Product, Category, Supplier
from user.serializers import LocationSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # nesting of serializers
    category_name = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'qty_stock', 'description', 'category_name']

    # creating product will automatically create category so thats why we are overriding create method
    def create(self, validated_data):
        category_data = validated_data.pop('category_name')
        category = CategorySerializer.create(CategorySerializer(), validated_data=category_data)
        product_instance = Product.objects.create(category_name=category, **validated_data)
        return product_instance

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category_name')
        category_name = instance.category_name
        category_name.name = category_data.get('name', category_name.name)
        category_name.description = category_data.get('description', category_name.name)
        category_name.save()

        instance.price = validated_data.get('price')
        instance.qty_stock = validated_data.get('qty_stock')
        instance.description = validated_data.get('description')
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id', 'company_name', 'phone_num', 'product','location_id']
