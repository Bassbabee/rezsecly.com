from django.db import models

class rezseclyURL(models.Model):
    url = models.CharField(max_length=254)
    shortcode = models.CharField(max_length=16, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
