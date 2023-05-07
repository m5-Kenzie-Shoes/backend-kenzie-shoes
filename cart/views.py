from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, get_object_or_404
from cart.serializers import ProductCartSerializer
from users.permissions import IsAccountOwner
from products.models import Product
from .models import ProductCart


class ProductCartView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = ProductCartSerializer
    queryset = ProductCart.objects.all()

    def perform_create(self, serializer):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))

        self.check_object_permissions(self.request, product)
        serializer.save(product=product, cart=self.request.user.cart)
