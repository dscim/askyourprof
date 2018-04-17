from django.db import models


class Subscribe(models.Model):
    subscribe = models.IntegerField(default=0)


class profStatus(models.Model):
    # false for busy and true for available
    button_status = models.BooleanField(default=True)
    schedule_status = models.BooleanField(default=True)
    sensor_status = models.BooleanField(default=True)
