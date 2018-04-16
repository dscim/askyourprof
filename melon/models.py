from django.db import models
from django.core.exceptions import ValidationError


from django.db import models


class Subscribe(models.Model):
    subscribe = models.IntegerField(default=0)

"""
https://alexpnt.github.io/2017/07/15/django-calendar/

class Event(models.Model):
    name = models.TextField('Name of the event', default='Event')
    day = models.DateField('Day of the event')
    start_time = models.TimeField('Starting time')
    end_time = models.TimeField('Final time')
    notes = models.TextField('Notes', blank=True, null=True)

    def __str__(self):
        return self.name

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:
            overlap = True
        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('End time must be after start time.')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError('There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
 """
