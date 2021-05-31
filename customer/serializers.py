from rest_framework.serializers import ModelSerializer

from customer.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
