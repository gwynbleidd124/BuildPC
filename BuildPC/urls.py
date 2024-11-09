from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Build.views import *
from BuildPC import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Build.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
