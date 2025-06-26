from django.contrib import admin
from .models import User  # Assuming you have a User model in users/models.py

admin.site.register(User)