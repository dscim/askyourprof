from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


def is_student(user):
    return user.groups.filter(name='Student').exists()


def is_professor(user):
    return 'professor' in user.groups


@login_required
def home(request):
    text = 'Welcome to the home page'
    context = {'text': text}
    return render(request, 'melon/home.html', context)


@login_required
@user_passes_test(is_student)
def studpage(request):
    return HttpResponse("This is the student page.")


@login_required
@user_passes_test(is_professor)
def profpage(request):
    return HttpResponse("This is the professor page.")
