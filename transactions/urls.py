from django.urls import path
from .views import DepositMoneyView, borrow_book

urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name='deposit'),
    path('borrow/', borrow_book, name='borrow_book'),
]
