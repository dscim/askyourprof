from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import profStatus, Subscribe


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
    sub = get_object_or_404(Subscribe, uname="gunilla") # hardcoded temp solution
    context = {
        'sub_count' : sub.subscribe,
    }
    return render(request, 'melon/profpage.html', context)

@login_required
@user_passes_test(is_student)
def subscribe_view(request):
    sub = Subscribe.objects.get(uname="gunilla") # hardcoded temp solution
    sub.subscribe += 1
    sub.save()
    return HttpResponse("You have been subscribed.")

