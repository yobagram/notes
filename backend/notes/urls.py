from rest_framework import routers

from .views import NoteViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
#router.register(r'^get_messages', NoteViewSet)
#router.register(r'get', NoteViewSet)
#router.register(r'api/mark_read', NoteReadSet)
#r'^api/v1/

# URLs настраиваются автоматически роутером
urlpatterns = router.urls