from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('view/update/<int:id>', views.update, name='update'),
    path('view/update/record/<int:id>', views.updaterecord, name='updaterecord'),
    path('sort/', views.sortcreate, name='sort'),
    path('view/delete/<int:id>', views.delete, name='delete')
]
