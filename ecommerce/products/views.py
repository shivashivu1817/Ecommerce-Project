from rest_framework import generics

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductSerializer
)


# Category List + Create
class CategoryListCreateView(
    generics.ListCreateAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Category Edit + Delete
class CategoryDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product List + Create
class ProductListCreateView(
    generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Edit + Delete
class ProductDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer