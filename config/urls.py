from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.static import STATIC_ROOT, STATIC_URL
from user.views import LoginView, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view()),
    path('api/register/', UserCreateView.as_view()),
] + static(STATIC_URL, document_root=STATIC_ROOT)

admin.site.site_header = "Cuidar.se Admin"
admin.site.site_title = "Cuidar.se Admin"
