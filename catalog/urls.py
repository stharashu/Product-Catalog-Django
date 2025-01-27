from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),          # Home view
    path('', views.product_list, name='product_list'),  # Product list view
    path('<int:pk>/', views.product_detail, name='product_detail'),  # Product detail view
]
