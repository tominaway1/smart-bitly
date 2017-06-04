from __future__ import unicode_literals

from django.db import models
from watson.models import Language

#import * from view.py

from bs4 import BeautifulSoup
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


    def _detect(self):
        if self.language is None:
            detected_language = None  # TODO: detect language using IBM Watson API
            self.language = detected_language

    def translate(self, lang_code):
        translated_source = None
        if translated_source is not None:
            translator = HtmlSourceTranslator(self.html_source, self.language)
            self.translation_dict[lang_code] = translator.translate(lang_code)

    def __unicode__(self):
        return self.url.name + "-" + self.language

