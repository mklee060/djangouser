# api/authentication/viewsets/check_token.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CheckTokenViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        return Response({"success": True}, status=status.HTTP_200_OK)
