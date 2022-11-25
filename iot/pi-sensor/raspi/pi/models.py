import datetime

from django.db import models
from django.utils import timezone

class WeatherReadings(models.Model):
    pub_time = models.DateTimeField('time published')
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_time >= timezone.now() - datetime.timedelta(days=1)


class ResponseTime(models.Model):
    weather_data = models.ForeignKey(WeatherReadings, on_delete=models.CASCADE)
    


    