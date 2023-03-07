from django.urls import path
from users import views

get_post = {'get': 'list', 'post': 'create'}
get_put_delete = {'get': 'retrieve', 'put': 'update',
                  'delete': 'destroy'}

urlpatterns = [
    path('account/<int:id>/', views.AccountViewSet.as_view(get_put_delete)),
]
