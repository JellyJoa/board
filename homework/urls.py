from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='my_main.html'), name='home'),
    # path('main/', TemplateView.as_view(template_name='my_main.html'), name='main'),
    path('admin/', admin.site.urls),
    path('sun/', include('sun.urls')),
    path('users/', include('users.urls'))
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
