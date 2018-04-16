from django.db import models
from django.core.exceptions import ValidationError


from django.db import models


class Subscribe(models.Model):
    subscribe = models.IntegerField(default=0)
