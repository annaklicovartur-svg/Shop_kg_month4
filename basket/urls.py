# basket/urls.py
from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    # Форма добавления товара
    path('basket_todo/', views.create_basket_view, name='create_basket'),
    
    # Список всех товаров (ГЛАВНАЯ СТРАНИЦА)
    path('basket_list/', views.read_basket_view, name='basket_list'),
    
    # Удаление товара
    path('basket_list/<int:id>/delete/', views.delete_basket_view, name='delete'),
]