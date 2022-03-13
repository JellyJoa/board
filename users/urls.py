from django.urls import path
from users import views
from django.views.generic.base import TemplateView

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('loginProcess/', views.login_process, name='login_process')
]
