from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from cart.serializers import ProductCartSerializer
from .permissions import IsBuyAccountOwner
from users.permissions import IsAccountOwner
from products.models import Product
from .models import Cart
from rest_framework.permissions import IsAuthenticated


class ProductCartView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductCartSerializer
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        print(self.request.data)
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))

        self.check_object_permissions(self.request, product)
        serializer.save(product=product, user=self.request.user)


class ProductCartDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsBuyAccountOwner]

    serializer_class = ProductCartSerializer
    queryset = Cart.objects.all()
