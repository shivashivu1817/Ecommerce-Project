from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Cart
from .serializers import CartSerializer


# GET Cart Items
# POST Add To Cart
class CartListCreateView(generics.ListCreateAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


# UPDATE Cart Quantity
class CartUpdateView(generics.UpdateAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(
            user=self.request.user
        )


# DELETE Cart Item
class CartDeleteView(generics.DestroyAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(
            user=self.request.user
        )