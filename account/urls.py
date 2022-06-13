from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('', views.signin, name='signin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
