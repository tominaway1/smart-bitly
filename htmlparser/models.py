from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class UrlProperties(models.Model):
    url = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url

    def _detect(self):
        pass  # TODO: detect language from original URL


class Html_Content(models.Model):
    url = models.ForeignKey(UrlProperties, null=False)
    html_source = models.TextField()
    language = models.CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.url.name + "-" + self.language