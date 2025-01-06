from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory, Dua
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Dua)