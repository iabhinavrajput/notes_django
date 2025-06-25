from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_note, name='add-note'),
    path('edit/<int:note_id>/', views.edit_notes, name='edit-note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete-note'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]