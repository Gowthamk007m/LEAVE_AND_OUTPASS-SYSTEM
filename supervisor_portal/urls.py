from django.urls import path
from . import views


urlpatterns = [


    path('supervisor_home/', views.supervisor_home, name='supervisor_home'),
    path('approve_request/<str:request_id>',
         views.approve_request, name='approve_request'),




]
