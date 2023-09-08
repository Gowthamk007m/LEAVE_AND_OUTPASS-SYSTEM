from django.shortcuts import render
import secrets
import string
from django.contrib import messages
from student_portal.models import Request
from django.shortcuts import render
from student_portal.forms import *

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def approve_leave_request(request, request_id):
    # Get the leave request object from the database
    leave_request = Request.objects.get(id=request_id)

    # Check if the user is authorized to approve or deny this request

    # Handle the form submission
    if request.method == 'POST':
        # Get the approval status from the form data
        is_approved = request.POST.get('is_approved')

        if is_approved == 'approved':
            # Update the leave request object with the new approval status
            leave_request.is_approved = True
            leave_request.is_denied = False

            # Generate a 4-digit alphanumeric system ID
            sys_id = ''.join(secrets.choice(
                string.ascii_uppercase + string.digits) for _ in range(6))
            leave_request.sys_id = sys_id

            leave_request.save()

            # Redirect the user back to the detail page of the leave request
            return redirect('mentor_home')
        elif is_approved == 'denied':
            # Update the leave request object with the new approval status
            leave_request.is_approved = False
            leave_request.is_denied = True

            leave_request.save()

            # Send a message to the student
            messages.warning(request, 'Your leave request has been denied.')

            # Redirect the user back to the detail page of the leave request
            return redirect('mentor_home')

    # Render the form for the warden to approve or deny the request
    return render(request, 'mentor/approve_leave_request.html', {'request': leave_request})


def mentor_home(request):
    # Get all pending leave requests
    pending_requests = Request.objects.filter(
        request_type='leave', is_approved=False, is_denied=False)

    # Render the warden's home page
    return render(request, 'mentor/mentor_home.html', {'pending_requests': pending_requests})
