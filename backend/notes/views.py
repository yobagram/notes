from django.shortcuts import render



# Create your views here.
from rest_framework import viewsets

from rest_framework import generics

from rest_framework.renderers import JSONRenderer


from .models import Note
from .serializers import NoteSerializer

#from django_filters.rest_framework import DjangoFilterBackend

#from notes.filters import GtIdFilter
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
    
# для удобстве введения данных через консоль командой
# POST "http://<URL>/api/notes/" <ARGS> 
class NoteViewSet(viewsets.ModelViewSet):    
    queryset = Note.objects.all().order_by('-id')
    serializer_class = NoteSerializer
    

#для запроса всех сообщений с id более указанного     
class NoteListSet(generics.ListAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        queryset = Note.objects.filter(read=False).order_by('-id')
        last_id = self.request.query_params.get('last_id', None)
        if last_id is not None:
            queryset = queryset.filter(id__gt=last_id)
        return queryset
    
    
#для помечания сообщения прочитанным
class NoteReadSet(generics.UpdateAPIView):
    serializer_class = NoteSerializer
    
    def post(self, request, format=None):
        #queryset = Note.objects.filter(read=False).order_by('-created_at')
        id = self.request.query_params.get('id', None)
        if id is not None:
            note = Note.objects.filter(id=id).first()
            if note is not None:
                note.read = True
                note.save()
        return Response([])
