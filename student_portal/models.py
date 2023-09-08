from django.db import models
from django.contrib.auth.models import User
from supervisor_portal.models import *



class Request(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50)
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    leave_date_start = models.DateField(null=True, blank=True)
    leave_date_end = models.DateField(null=True, blank=True)
    outing_hours = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sys_id = models.CharField(max_length=50,null=True)
