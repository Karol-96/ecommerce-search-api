from django.urls import path
from .views import ListCategory, DetailCategory , ListBooks, DetailBooks , ListProduct, DetailProduct


urlpatterns = [

    path('categories',ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view() , name ='singlecategory'),
    path('books',ListBooks.as_view(), name = 'books'),
    path('books/<int:pk>/',DetailBooks.as_view(),name='singlebooks'),
    path('product',ListProduct.as_view(),name='product'),
    path('product/<int:pk>/',DetailBooks.as_view(),name='singleproduct'),
]