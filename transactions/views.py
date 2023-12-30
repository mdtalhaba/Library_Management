from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from datetime import datetime
from django.db.models import Sum
from transactions.forms import DepositForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from transactions.models import DepositUser
from books.models import Book
from .models import BorrowBook
from django.urls import reverse


def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {'user': user, 'amount' : amount})
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class DepositMoneyView(LoginRequiredMixin, CreateView):
    form_class = DepositForm
    model = DepositUser
    template_name = 'transactions/deposit_form.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        # if not account.initial_deposit_date:
        #     now = timezone.now()
        #     account.initial_deposit_date = now
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(self.request.user, amount, 'Deposit Message', 'transactions/deposit_email.html')
        return super().form_valid(form)


def borrow_book(req, book_id):
    book = Book.objects.get(id=book_id)
    borrowbook = BorrowBook(account=req.user.account, book=book)
    borrowbook.save()
    current_url = reverse('book_details', args=[book_id])
    return redirect(current_url)