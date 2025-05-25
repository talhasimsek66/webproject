from django.urls import path
from . import views

app_name = "forum"
urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:id>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:id>/delete', views.post_delete, name="post_delete"),
]