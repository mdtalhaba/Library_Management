from django.contrib import admin
from  category.models import Category

class CategoryAdmin(admin.ModelAdmin) :
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)