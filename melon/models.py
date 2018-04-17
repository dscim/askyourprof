from django.db import models


class Subscribe(models.Model):
    uname = models.TextField(default="")
    subscribe = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.uname


class profStatus(models.Model):
    # false for busy and true for available
    uname = models.TextField(default="")
    button_status = models.BooleanField(default=True)
    schedule_status = models.BooleanField(default=True)
    sensor_status = models.BooleanField(default=True)
    objects = models.Manager()

    def getStatus(self):
        if self.button_status and self.schedule_status and self.sensor_status:
            return True
        else:
            return False
    
    def __str__(self):
        return self.uname
