from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import profStatus, Subscribe
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("ttm4115/team18/", qos=2)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(data)

client = mqtt.Client("webserver_team18", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883)
        
client.loop_start()

def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_professor(user):
    return user.groups.filter(name='Professors').exists()


def home(request):
    return render(request, 'melon/cover.html')

@login_required
def view_prof(request, uname):
    prof = profStatus.objects.get(uname=uname)
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
    sub = Subscribe.objects.get(uname="gunilla")
    status = profStatus.objects.get(uname="gunilla")
    context = {
        'sub_count' : sub.subscribe,
        'button_status' : status.button_status,
    }
    return render(request, 'melon/profpage.html', context)

@login_required
@user_passes_test(is_student)
def subscribe_view(request):
    sub = Subscribe.objects.get(uname="gunilla")
    sub.subscribe += 1
    sub.save()
    return render(request, 'melon/subscribe_view.html')

@login_required
@user_passes_test(is_professor)
def press_busy(request):
    button = profStatus.objects.get(uname="gunilla")
    button.button_status = False
    button.save()
    client.publish("ttm4115/team18/", json.dumps({"user_id": "gunilla", "type": "button", "status": "busy"}), qos=2)
    return render(request, 'melon/redirect.html')

@login_required
@user_passes_test(is_professor)
def press_available(request):
    button = profStatus.objects.get(uname="gunilla")
    button.button_status = True
    button.save()
    client.publish("ttm4115/team18/", json.dumps({"user_id": "gunilla", "type": "button", "status": "available"}), qos=2)
    return render(request, 'melon/redirect.html')
