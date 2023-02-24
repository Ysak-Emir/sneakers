from django.urls import path
from users import views

urlpatterns = [
    path('personal_account/<int:id>/', views.AccountListAPIView.as_view())
]
