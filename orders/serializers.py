from rest_framework import serializers
from .models import UserOrder
from .models import UserOrder, OrderStatus


class OrderSerializer(serializers.ModelSerializer):

    user_buy = serializers.EmailField(source="user.email", read_only=True)
    status = serializers.ChoiceField(choices=OrderStatus.choices,
                                     default=OrderStatus.REALIZADO)

    class Meta:
        
        model = UserOrder
        fields = [
            "id",
            "status",
            "buyed_at",
            "user_buy",
            "products",
        ]

        read_only_fields = ["id", "buyed_at", "products"]