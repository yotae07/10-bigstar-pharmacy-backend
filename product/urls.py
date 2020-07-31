from django.urls import path
from .views import ProductMainView, ProductDetailView

urlpatterns = [
    path('product/detail/<int:id>', ProductDetailView.as_view()),
    path('produt', ProductMainView.as_view()),
]
