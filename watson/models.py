from __future__ import unicode_literals

from django.db import models
import uuid

class Language(models.Model):
    name = models.CharField(max_length=100)
    language_code = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url