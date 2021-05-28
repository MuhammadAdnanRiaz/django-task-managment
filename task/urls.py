from django.urls import path, include
from rest_framework import routers
from .views import TaskView

router = routers.DefaultRouter()
router.register('', TaskView, basename="Task")
urlpatterns = [
    path('', include(router.urls))
]
