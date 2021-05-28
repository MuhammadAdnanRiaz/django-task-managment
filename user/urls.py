from django.urls import path, include
from .views import RegisterView, LoginView
from knox import views as knox_views

urlpatterns = [
    path('register/',
         RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout')
]
