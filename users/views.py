from rest_framework import status
from rest_framework.response import Response
from users.serializer import AccountSerializer, AccountValidateSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from users.models import Account


class AccountListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'
