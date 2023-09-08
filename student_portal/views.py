from .models import Request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RequestForm


def home(request):
    return render(request,'student_portal/student_home.html')

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.student = request.user
            request_obj.save()

            # Save the Request object in the session
            request.session['request_obj_id'] = request_obj.id

            if request_obj.request_type in ['outing', 'extended_outing']:
                return redirect('time')
            else:
                return redirect('view_requests')
    else:
        form = RequestForm()
    return render(request, 'student_portal/create_request.html', {'form': form})


@login_required
def time(request):
    try:
        request_obj = Request.objects.get(pk=request.session['request_obj_id'])
    except (KeyError, Request.DoesNotExist):
        return redirect('create_request')

    if request.method == 'POST':
        outing_hours = request.POST.get('outing_hours')
        request_obj.outing_hours = outing_hours
        request_obj.save()
        return redirect('view_requests')

    return render(request, 'student_portal/time.html', {'request_obj': request_obj})


@login_required
def view_requests(request):
    requests = Request.objects.filter(
        student=request.user).order_by('-created_at')
    return render(request,'student_portal/view_requests.html', {'requests': requests})


