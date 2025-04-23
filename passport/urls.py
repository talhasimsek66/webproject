
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index),
    path('countries/', views.country_list),
    path('passport/',views.passport_list),
    path('filter/', views.filter_by_passport, name='filter_by_passport'),
    path('add-country/', views.add_country, name='add_country'),

]