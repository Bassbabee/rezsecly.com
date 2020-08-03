from django.db import models
from django.conf import settings

from .utils import create_shortcode
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 16)

class rezseclyURLManager(models.Manager):
    ''' Show only active usrls '''
    def all(self, *args, **kwargs):
        return super(rezseclyURLManager, self).all(*args, **kwargs).filter(active=True)

    # use RezseclyURL.objects.example_for_manager()
    def example_for_manager(self):
        pass

class RezseclyURL(models.Model):
    url = models.CharField(max_length=254, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    # update RezseclyURL manager with our new manager
    objects = rezseclyURLManager()

    def get_short_url(self):
        return "http://127.0.0.1:8000/{shortcode}".format(shortcode=self.shortcode)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(RezseclyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
