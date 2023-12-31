from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    borrowing_price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='books/media/uploads/')
    user_reviews = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model) :
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

