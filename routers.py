# api/routers.py

from api.authentication.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    ActiveSessionViewSet,
    LogoutViewSet,
    CheckTokenViewSet,  # new import
)
from rest_framework import routers
from api.user.viewsets import UserViewSet
from api.naics_search.viewsets import NaicsSearchView

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"edit", UserViewSet, basename="user-edit")

router.register(r"register", RegisterViewSet, basename="register")

router.register(r"login", LoginViewSet, basename="login")

router.register(r"checkSession", ActiveSessionViewSet, basename="check-session")

router.register(r"logout", LogoutViewSet, basename="logout")

router.register(r"checkToken", CheckTokenViewSet, basename="checkToken")  # new endpoint

# Register NaicsSearchView
router.register(r"naics_search", NaicsSearchView, basename="naics-search")

urlpatterns = [
    *router.urls,
]
