from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.food),
    path('timeset/', views.timeset),
    path('products_list/', views.products),
    path('products_list/<int:id>/', views.products_detail),
]