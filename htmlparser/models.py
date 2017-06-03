from __future__ import unicode_literals

from django.db import models
from watson.models import Language
from bs4 import BeautifulSoup
import uuid

tag_separator = '_#!@(0_2|%'

# Create your models here.
class UrlProperties(models.Model):
    url = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.url


class HtmlSourceTranslator:
    source = None
    source_lang_code = None
    soup_obj = None

    def __init__(self, html_source, source_lang_code):
        self.source = html_source
        self.source_lang_code = source_lang_code
        self.soup_obj = BeautifulSoup(html_source, 'html.parser')

    def translate(self, lang_code):
        paragraphs_arr = list()
        for paragraph in self.soup_obj.find_all('p'):
            paragraphs_arr.push(paragraph)
        translation_txt = tag_separator.join(paragraphs_arr)
        translated_text = None  # TODO: translate content to another language
        translated_paragraphs = translated_text.split(paragraphs_arr)
        translated_soup = BeautifulSoup(self.html_source, 'html.parser')
        for idx, paragraph in enumerate(translated_soup.find_all('p')):
            paragraph.string.replace_with(translated_paragraphs[idx])
        return translated_soup.prettify()


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
        translated_source = None
        if translated_source is not None:
            translator = HtmlSourceTranslator(self.html_source, self.language)
            self.translation_dict[lang_code] = translator.translate(lang_code)

    def __unicode__(self):
        return self.url.name + "-" + self.language

