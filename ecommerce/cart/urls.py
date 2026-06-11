from django.urls import path

from .views import (
    CartListCreateView,
    CartUpdateView,
    CartDeleteView,
)

urlpatterns = [

    path(
        '',
        CartListCreateView.as_view()
    ),

    path(
        '<int:pk>/update/',
        CartUpdateView.as_view()
    ),

    path(
        '<int:pk>/delete/',
        CartDeleteView.as_view()
    ),

]