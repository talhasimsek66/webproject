from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add_comment/', views.add_comment, name='add_comment'),
]