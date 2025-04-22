
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index),
    path('exchange/',views.exchange),
    path('countries/', views.country_list),
    path('passport/',views.passport_list),
    path('ordinary/', views.ordinarypass ),

    path('special/', views.specialpass),
    path('filter/', views.filter_by_passport, name='filter_by_passport'),
    path('forum/', views.forum),

]