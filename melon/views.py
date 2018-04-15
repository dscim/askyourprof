from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_professor(user):
    return user.groups.filter(name='Professors').exists()


@login_required
def home(request):
    return render(request, 'melon/cover.html')


@login_required
@user_passes_test(is_student)
def studpage(request):
    return HttpResponse("This is the student page.")


@login_required
@user_passes_test(is_professor)
def profpage(request):
    return render(request, 'melon/fullcalendar.html')
