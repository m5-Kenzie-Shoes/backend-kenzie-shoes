from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views as jwt_views
from orders.views import OrderView, OrderDetailView, BuyOrderView, SellOrderView, BuyOrderDetailView, SellOrderDetailView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/orders/", OrderView.as_view()),
    path("users/buyorders/", BuyOrderView.as_view()),
    path("users/buyorders/<int:pk>/", BuyOrderDetailView.as_view()),
    path("users/sellorders/", SellOrderView.as_view()),
    path("users/sellorders/<int:pk>/", SellOrderDetailView.as_view()),
    path("users/orders/<int:pk>/", OrderDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
