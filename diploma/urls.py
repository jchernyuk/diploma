from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from diploma import settings
from learning.views import IndexView


def error404(request, exception):
    return render(request, '404.html')


handler404 = error404

urlpatterns = [
    path('', IndexView.as_view(), name='mainpage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls', namespace='user')),
    path('', include('learning.urls', namespace='learning')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
