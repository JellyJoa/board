from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='my_main.html'), name='main'),
    path('main/', TemplateView.as_view(template_name='my_main.html'), name='main'),
    path('admin/', admin.site.urls),
    path('login/', TemplateView.as_view(template_name='log_in.html'), name='login'),
    path('sun/', include('sun.urls'))
]
