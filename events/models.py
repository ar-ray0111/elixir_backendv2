from django.db import models

CHOICES = [
    ('GFG', 'GFG'),
    ('CC', 'CC'),
    ('GDSC', 'GDSC')
]



# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    event_summary = models.TextField()
    form_link = models.URLField()
    date = models.DateField()
    img_link = models.URLField()
    club = models.CharField(choices=CHOICES, default='GFG')

    def __str__(self):
        return self.name
