from django.urls import path
from .views import *

urlpatterns = [
    path("products", product_list, name="product_list"),
    path("products/<int:pk>", product_detail, name = "product_detail")
]