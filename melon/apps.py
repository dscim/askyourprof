from django.apps import AppConfig
import paho.mqtt.client as mqtt
import json


class MelonConfig(AppConfig):
    name = 'melon'

    def ready(self):
        from .models import profStatus

        def on_connect(client, userdata, flags, rc):
            client.subscribe("ttm4115/team18/", qos=2)

        def on_message(client, userdata, msg):
            data = json.loads(msg.payload.decode())
            prof = profStatus.objects.get(uname=data['user_id'])
            print(data)
            
            if data['type'] == 'schedule':
                if data['status'] == 'busy':
                    prof.schedule_status = False
                elif data['status'] == 'available':
                    prof.schedule_status = True
                else:
                    print('unrecognized type status')
            elif data['type'] == 'button':
                if data['status'] == 'busy':
                    prof.button_status = False
                elif data['status'] == 'available':
                    prof.button_status = True
                else:
                    print('unrecognized type status')
            elif data['type'] == 'sensor':
                if data['status'] == 'busy':
                    prof.sensor_status = False
                elif data['status'] == 'available':
                    prof.sensor_status = True
                else:
                    print('unrecognized type status')
            else:
                print('unrecognized type value')
            
            prof.save()
            

        client = mqtt.Client("webserver_team18", clean_session=False)
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("test.mosquitto.org", 1883)
        
        client.loop_start()
