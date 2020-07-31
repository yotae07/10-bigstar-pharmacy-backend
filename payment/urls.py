from django.urls import path

from .views import PaymentView, PaymentTogo, MyPillyView

urlpatterns = [
    path('payment',PaymentView.as_view(), name='payment'),
    path('payment/togo', PaymentTogo.as_view(), name='payment_togo'),
    path('my-pilly', MyPillyView.as_view(), name='mypilly'),
]

