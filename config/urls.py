from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from status.views import AnnotationViewSet
from user.views import LoginView, UserCreateView, UserViewSet

from config.static import STATIC_ROOT, STATIC_URL

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('annotation', AnnotationViewSet, basename='annotation')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view()),
    path('api/register/', UserCreateView.as_view()),
] + static(STATIC_URL, document_root=STATIC_ROOT)

admin.site.site_header = "Cuidar.se Admin"
admin.site.site_title = "Cuidar.se Admin"
