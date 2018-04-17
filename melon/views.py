from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import profStatus


def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_professor(user):
    return user.groups.filter(name='Professors').exists()


def home(request):
    return render(request, 'melon/cover.html')

@login_required
def view_prof(request, uname):
    prof = get_object_or_404(profStatus, uname=uname)
    context = {
        'status' : prof.getStatus,
    }
    return render(request, 'melon/professor.html', context)


@login_required
@user_passes_test(is_student)
def studpage(request):
    return render(request, 'melon/students.html')


@login_required
@user_passes_test(is_professor)
def profpage(request):
    return render(request, 'melon/profpage.html')
