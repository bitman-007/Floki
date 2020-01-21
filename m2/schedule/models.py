from django.db import models


class Schedule(models.Model):
    day = (
        ('SUN', 'sunday'),
        ('MON', 'monday'),
        ('TUE', 'tuesday'),
        ('WED', 'wednssday'),
        ('THU', 'thursday'),)
    subject_name = models.CharField(max_length=30)
    date = models.CharField(max_length=3, choices=day)  # the day ex : sunday ,monday , ..etc
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor_name = models.CharField(max_length=30)
    subject_grade = models.IntegerField()
