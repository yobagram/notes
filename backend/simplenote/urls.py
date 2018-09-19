"""it_sol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
#from notes.filters import GtIdFilter
from notes.models import Note
#from notes.views import mark_read
import notes.views

#from django_filters.views import FilterView

urlpatterns = [
    path(r'api/', include('notes.urls')),
    #path(r'^get_messages', FilterView.as_view(filterset_class=GtIdFilter,)),
    #path(r'get_messages', FilterView.as_view(filterset_class=GtIdFilter,
    #path(r'api/get_messages/', FilterView.as_view(filterset_class=GtIdFilter,
    #                                 template_name='note_filter.html')),
    #path(r'api/mark_read)', notes.views.NoteReadView.as_view()),
    #path(r'api/mark_read', notes.views.NoteReadSet.as_view({'get': 'list'})),
    #path(r'get_messages', notes.views.NoteNewSet.as_view()),
    path(r'api/get_messages', notes.views.NoteNewSet.as_view()),
    path(r'api/mark_read', notes.views.NoteReadSet.as_view()),
    path(r'admin/', admin.site.urls),
]
