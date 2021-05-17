from django.contrib import admin
from .models import Category , Books , Product

# Register your models here.


admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Product)
