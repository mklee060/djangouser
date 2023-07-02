import jwt
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from api.authentication.models import ActiveSession
# import logging
# logger = logging.getLogger(__name__)
def _generate_jwt_token(user):
    token = jwt.encode(
        {"id": user.pk, "exp": datetime.utcnow() + timedelta(minutes=60)},
        settings.SECRET_KEY,
    )
    # logger.info(f"Issued token: {token}")  # log the issued token
    return token

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise exceptions.ValidationError(
                {"success": False, "msg": "Email is required to login"}
            )
        if password is None:
            raise exceptions.ValidationError(
                {"success": False, "msg": "Password is required to log in."}
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed({"success": False, "msg": "Wrong credentials"})

        if not user.is_active:
            raise exceptions.ValidationError(
                {"success": False, "msg": "User is not active"}
            )

        sessions = ActiveSession.objects.filter(user=user)

        if sessions.exists():
            # If there are any existing sessions for this user, delete them.
            sessions.delete()

        # Now create a new session for the user.
        session = ActiveSession.objects.create(
            user=user, token=_generate_jwt_token(user)
        )

        return {
            "success": True,
            "token": session.token,
            "user": {"_id": user.pk, "username": user.username, "email": user.email},
        }
