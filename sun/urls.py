from django.urls import path
from sun import views
from django.views.generic.base import TemplateView

app_name = 'sun'

# http://127.0.0.1:8000/sun/
urlpatterns = [
    path('tip/', views.b_tip, name='b_tip'),
    path('create/', views.create, name='create'),
    path('<int:board_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:board_id>/delete/', views.b_delete, name='b_delete'),
    path('<int:board_id>/edit/', views.b_edit, name='b_edit'),
    path('<int:board_id>/like/', views.b_like, name='b_like'),
    path('createComment/', views.create_comment, name='create_comment'),
    path('commentDelete/', views.delete_comment, name='delete_comment'),
    path('adopt/', TemplateView.as_view(template_name='adopt.html'), name='adopt'),
]