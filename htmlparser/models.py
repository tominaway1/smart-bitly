from __future__ import unicode_literals

from django.db import models
from watson.models import Language

import uuid



# Create your models here.
class UrlProperties(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url

class HtmlContent(models.Model):
    url = models.ForeignKey(UrlProperties, null=False)
    html_source = models.TextField()
    language = models.ForeignKey(Language, null=False)


    def __unicode__(self):
        return self.url.url+ "-" + self.language.language_code

