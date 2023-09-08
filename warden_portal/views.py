from django.shortcuts import render

from student_portal.models import Request

# Create your views here.


def warden_home(request):
    requests_A = Request.objects.filter(is_approved=True)
    requests_B = Request.objects.filter(is_denied=True)

    return render(request, 'warden/warden_home.html', {'requests_A': requests_A, 'requests_B': requests_B})
