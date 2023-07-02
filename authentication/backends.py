import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from api.user.models import User
from api.authentication.models import ActiveSession
# import logging
# Create a logger
# logger = logging.getLogger(__name__)
class ActiveSessionAuthentication(authentication.BaseAuthentication):

    auth_error_message = {"success": False, "msg": "User is not logged on."}

    def authenticate(self, request):

        request.user = None

        auth_header = authentication.get_authorization_header(request)

        if not auth_header:
            return None

        token = auth_header.decode("utf-8")
        # logger.info(f'Received token: {token}')  # Log the received token

        return self._authenticate_credentials(token)

    def _authenticate_credentials(self, token):
        #### ADDDED THIS TOKEN SPLIT PART#### because decodeing problem
        # Split the token on space and take the second part
        if token and ' ' in token:
            token = token.split()[1]
        ####################################
        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except:
            # logger.error('Failed to decode token')  # Log an error message
            raise exceptions.AuthenticationFailed(self.auth_error_message)

        try:
            active_session = ActiveSession.objects.get(token=token)
        except:
            # logger.error('Failed to get active session')  # Log an error message
            raise exceptions.AuthenticationFailed(self.auth_error_message)

        try:
            user = active_session.user
        except User.DoesNotExist:
            msg = {"success": False, "msg": "No user matching this token was found."}
            # logger.error('No user matching this token was found')  # Log an error message
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = {"success": False, "msg": "This user has been deactivated."}
            # logger.error('This user has been deactivated')  # Log an error message
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
