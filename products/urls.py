from django.urls import path
from products.views import history_remove, ProductsListAPIView, history_detail, history_add,\
    product_delete_view, product_view, history_clear


urlpatterns = [
    path('productlist/', ProductsListAPIView.as_view()),
    path('history_remove/', history_remove),
    path('history_detail/', history_detail),
    path('history_add/', history_add),
    path('product_view/', product_view),
    path('product_delete/', product_delete_view),
    path('history_clear/', history_clear),
]