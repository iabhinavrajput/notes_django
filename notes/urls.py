from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_note, name='add-note'),
    path('edit/<int:note_id>/', views.edit_notes, name='edit-note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete-note'),
]