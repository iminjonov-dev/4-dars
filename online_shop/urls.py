from django.urls import path
from online_shop import views
urlpatterns = [
    path('index/', views.products_list, name='product'),
    path('index/detail/', views.products_all_view, name='products'),

]
