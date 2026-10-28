from django.urls import path
from . import views

urlpatterns = [
    path('', views.unis_list , name = 'unis_list'),
    path('create/', views.unis_create , name = 'unis_create'),
    path('<int:Unis_id>/edit/', views.unis_edit , name = 'unis_edit'),
    path('<int:Unis_id>/delete/', views.unis_delete , name = 'unis_delete'),
    path('register/', views.register , name = 'register'),

]