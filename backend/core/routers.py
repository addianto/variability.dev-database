from rest_framework import routers

from core.fileupload.views import FileUploadSetView
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

# routes = SimpleRouter()
router = routers.DefaultRouter()

# AUTHENTICATION
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'files', FileUploadSetView)

# USER
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls
]
