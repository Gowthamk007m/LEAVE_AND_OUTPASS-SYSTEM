from django.urls import path
from . import views


urlpatterns = [

    path('mentor_home/', views.mentor_home, name='mentor_home'),
    path('approve_leave_request/<str:request_id>',
         views.approve_leave_request, name='approve_leave_request'),
         
]
