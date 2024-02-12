from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .api import api
from home import views
from .views import (
    login_view,
    register_user,
    logout_view,
)
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_view, name="logout"),
    path("", views.index, name="home"),
    path("api/", api.urls),
    re_path(r"^.*\.*", views.pages, name="pages"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)