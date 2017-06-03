from __future__ import unicode_literals

from django.db import models
from watson.models import Language
import uuid


# Create your models here.
class UrlProperties(models.Model):
    url = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url


class HtmlContent(models.Model):
    url = models.ForeignKey(UrlProperties, null=False)
    html_source = models.TextField()
    language = models.ForeignKey(Language, null=False)
    translation_dict = {}

    def __init__(self):
        self._detect()
        if self.language is not None:
            self.translation_dict[self.language] = self.html_source

    def _detect(self):
        if self.language is None:
            detected_language = None  # TODO: detect language using IBM Watson API
            self.language = detected_language

    def translate(self, lang_code):
        translated_source = None  # TODO: translate content to another language
        if translated_source is not None:
            self.translation_dict[lang_code] = translated_source

    def __unicode__(self):
        return self.url.name + "-" + self.language