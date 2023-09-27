from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

    class Meta:
        verbose_name_plural = "Airports"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"Flight from {self.origin} to {self.destination}"

    def calculate_flight_time(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours}h {minutes}m"

    class Meta:
        verbose_name_plural = "Flights"
