from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from robots import views

urlpatterns = [
    path('', include('robots.urls')),
    path('admin/', admin.site.urls),
    path('generate_excel_summary/', views.generate_excel_summary, name='generate_excel_summary'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

