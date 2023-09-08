from django.urls import path
from . import views


urlpatterns = [

    path('home/', views.home, name='stud_home'),
    path('create-request/', views.create_request, name='create_request'),
    path('view-requests/', views.view_requests, name='view_requests'),
    path('time/',views.time, name='time'),

]
