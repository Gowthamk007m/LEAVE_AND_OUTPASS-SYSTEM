from django.urls import path
from . import views


urlpatterns = [
    path('warden_home/', views.warden_home, name='warden_home'),
]
