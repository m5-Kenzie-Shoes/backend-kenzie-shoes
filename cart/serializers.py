from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from products.models import Product
from .models import Cart


class ProductCartSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        product = Product.objects.get(id=instance.product.id)
        quantity = product.stock - validated_data["quantities"]
        if quantity < 0:
            raise ValidationError({"detail": "Quantidade de produto indisponível"})
        return super().update(instance, validated_data)

    class Meta:
        model = Cart
        fields = ["id", "quantities", "user_id", "product"]

        read_only_fields = ["id", "user_id", "product"]

