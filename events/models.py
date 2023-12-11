from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    event_summary = models.TextField()
    form_link = models.URLField()
    date = models.DateField()
    img_link = models.URLField()

    def __str__(self):
        return self.name
