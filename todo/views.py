from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
