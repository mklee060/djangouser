from api.user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ["date", "id", "username", "email", 'microsoft_upn', 'is_paid_user']
        read_only_field = ["id"]


# original
# from api.user.models import User
# from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(read_only=True)

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "date"]
#         read_only_field = ["id"]
