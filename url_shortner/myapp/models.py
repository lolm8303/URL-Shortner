from django.db import models
from .utils import getId

class Website(models.Model):
    longurl = models.URLField()
    shorturl = models.CharField(blank = True, unique = True, max_length = 20)

    def save(self, *args, **kwargs):
        if not self.shorturl:
            self.shorturl = getId(self, 5)
        
        super().save(*args, **kwargs)