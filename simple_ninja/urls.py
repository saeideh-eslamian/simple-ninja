# project/urls.py (e.g., simple_ninja/urls.py)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from crud_ninja.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_ninja.urls', namespace='crud_ninja')),
    path('api/', api.urls)
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
