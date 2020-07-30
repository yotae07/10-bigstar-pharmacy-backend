from django.urls import path
from .views import CartAdd, CartView, Count, DeleteItem

urlpatterns = [
    path('cart', CartAdd.as_view(), name='cart'),
    path('cartview', CartView.as_view(), name='cartview'),
    path('cartview/count', Count.as_view(), name='count'),
    path('cartview/delete', DeleteItem.as_view(), name='delete')
]
