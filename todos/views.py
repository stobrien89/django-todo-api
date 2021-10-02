from models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    # main query for the index route
    query_set = Todo.objects.all()
    # serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class to set permission level
    # could be [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
