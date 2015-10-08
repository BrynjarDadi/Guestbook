import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Text(models.Model):
    name = models.CharField(max_length=200,default="")
    guestbook_text = models.TextField(default="")
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
