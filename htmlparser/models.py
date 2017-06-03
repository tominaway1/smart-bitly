from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class UrlProperties(models.Model):
    url = models.CharField(max_length=100)
    html_source = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url