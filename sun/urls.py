from django.urls import path
from sun import views
from django.views.generic.base import TemplateView

# http://127.0.0.1:8000/sun/
urlpatterns = [
    path('tip/', views.b_tip, name='b_tip'),
    path('create/', views.create, name='create'),
    path('<int:board_id>/detail/', views.b_detail, name='b_detail')
]