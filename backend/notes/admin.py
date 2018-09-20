from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Note

#добавляем класс администрирования, чтобы иметь доступ к админке Django
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note)