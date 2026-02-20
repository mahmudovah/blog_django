from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_pro_list, name='pro_list'),
]