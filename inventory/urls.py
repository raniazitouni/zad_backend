from django.urls import path
from . import views 

urlpatterns = [
    path('Products/', views.Products.as_view(), name='Products'),
    path('add/', views.AddProduct.as_view(), name='add-product'),
    path('delete/<int:product_id>/', views.DeleteProduct.as_view(), name='delete-product'),
    path('update/<int:product_id>/', views.UpdateProduct.as_view(), name='update-product'),
]