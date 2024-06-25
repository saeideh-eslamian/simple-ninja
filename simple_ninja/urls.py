from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('crud_ninja.urls', namespace='crud_ninja'))
]
