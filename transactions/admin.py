from django.contrib import admin
from .models import DepositUser, BorrowBook

admin.site.register(DepositUser)
admin.site.register(BorrowBook)
