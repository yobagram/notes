from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Note

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note)