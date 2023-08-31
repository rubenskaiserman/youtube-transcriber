from django.contrib import admin
from django.urls import path
from .views import hello_world
from transcriber import views as transcriber_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls), # Should be removed in production
    path('', hello_world, name='hello_world'),
    path('upload', transcriber_views.upload, name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
