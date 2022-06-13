
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.index), name='index'),
    path("create", login_required(views.create), name='create'),
    path("create-dataset", login_required(views.create_dataset), name='createdataset'),
    path('delete/<int:pk>/', login_required(views.delete), name='delete'),
    path('dataset', login_required(views.index_dataset), name='dataset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
