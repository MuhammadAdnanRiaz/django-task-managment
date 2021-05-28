from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_queryset(self):
        print(self.request)
        return Task.objects.filter(user=self.request.user)
