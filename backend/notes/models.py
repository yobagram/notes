from django.db import models

# Create your models here.


# Модель записи
#text - текст
#read - булевая переменная прочитано или нет
#created_at - дата создания, заполняется автоматически
class Note(models.Model):
    text = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)