from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .api import api

app_name = 'crud_ninja'
urlpatterns = [
    path('api/', api.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)