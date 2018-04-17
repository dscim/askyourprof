from django.db import models


class Subscribe(models.Model):
    subscribe = models.IntegerField(default=0)


class profStatus(models.Model):
    # false for busy and true for available
    uname = models.TextField(default="")
    button_status = models.BooleanField(default=True)
    schedule_status = models.BooleanField(default=True)
    sensor_status = models.BooleanField(default=True)

    def getStatus(self):
        if self.button_status and self.schedule_status and self.sensor_status:
            return True
        else:
            return False
    
    def __str__(self):
        return self.uname
