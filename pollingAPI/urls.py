from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pollingAPI_app.urls')),
    path('api/auth/', include('authentication.urls')),
]
