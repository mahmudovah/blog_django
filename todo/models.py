from django.db import models
from datetime import datetime, timedelta
import calendar

now = datetime.now

class Todo(models.Model):
    body = models.TextField(blank=True)
    duration = models.FloatField()

    status_choice = (
        ("min", "daqiqa"),
        ("hour", "soat"),
        ("day", "kun"),
        ("week", "hafta"),
        ("month", "oy"),
        ("year", "yil")
    )
    type_choice = (
        ("new", "Yangi"),
        ("proccesing", "Davom etmoqda"),
        ("done", "Bajarildi")    
    )
    duration_type =models.CharField(max_length=15, choices=type_choice)
    status = models.CharField(max_length=10, choices=status_choice)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:30]
    
    def duration_range(self):
        if self.duration_type == "min":
            return self.created_at + timedelta(minutes=self.duration)
        
        if self.duration_type == "hour":
            return self.created_at + timedelta(hours=self.duration)
        
        if self.duration_type == "day":
            return self.created_at + timedelta(days=self.duration)
            
        if self.duration_type == "week":
            return self.created_at + timedelta(weeks=self.duration)
        
        if self.duration_type == "month":
            year = datetime.now().year
            month = datetime.now().month
            first_day, days_count = calendar.monthrange(year, month)
            return self.created_at + timedelta(days=days_count)
        
        if self.duration_type == "year":
            year = datetime.now().year
            if year % 4 == 0:
                day = 366
            else:
                day = 365

            return self.created_at + timedelta (days=day)

        