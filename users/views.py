from rest_framework import status
from rest_framework.response import Response
from users.serializer import AccountSerializer, AccountValidateSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Account


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AccountValidateSerializer
        else:
            return AccountSerializer
