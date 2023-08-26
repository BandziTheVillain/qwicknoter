from rest_framework import viewsets, permissions, pagination
from .serializers import NoteSerializer
from notes.models import Note

class NotesPagination(pagination.LimitOffsetPagination):
    default_limit = 25
    offset_query_param = "skip"

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        return True if obj.user == request.user else False

class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsUser,)
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by("-timestamp")
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)