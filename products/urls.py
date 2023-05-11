from django.urls import path
from .views import ProductView, ProductDetailView
from cart.views import ProductCartView

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<int:pk>/cart/", ProductCartView.as_view()),
]
