from django.http import HttpResponse
from django.shortcuts import render
import requests,json,urllib
from django.views.decorators.csrf import csrf_exempt
from models import UrlProperties, HtmlContent
from watson.models import Language
from urlparse import urlparse
from uuid import UUID
from bs4 import BeautifulSoup


def getDomainFromUrl(url):
    parsed_uri = urlparse(url)
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

def index(request):
    languageCode = "es"

    language = Language.objects.filter(language_code = languageCode).first()

    src = HtmlContent.objects.all()[0]
    hst = HtmlSourceTranslator(src.html_source,src.language.language_code);

    domain = getDomainFromUrl(request.build_absolute_uri())
    texts = hst.getTextToBeTranslated('p')
    translatedTexts = [None] *  len(texts)
    for i in range(len(texts)):
        text = texts[i]
        translatedTexts[i] = translate(domain, text, languageCode)
    translatedHtmlSource = hst.createTranslatedHtml(translatedTexts,'p').replace("href=\"","href=\"" + getDomainFromUrl(src.url.url))

    content = HtmlContent.objects.filter(url=src.url, language=language).first()
    if content is None:
        content = HtmlContent.objects.create(language=language, html_source=translatedHtmlSource, url=src.url)
    else:
        content.html_source = translatedHtmlSource
    content.save()

    return render(request,'home/index.html')

@csrf_exempt
def create_url(request):
    url = None
    if request.method == 'POST':
        url = request.POST.get("url", "")

    urlObj = UrlProperties.objects.create()
    urlObj.url = url
    urlObj.save()

    response_data = { 'url' : str(urlObj.uuid) }


    return HttpResponse(json.dumps(response_data), content_type="application/json")

def read_url(request,uuid):
    urlObj = UrlProperties.objects.filter(uuid = UUID(uuid)).first()

    html = get_html_from_link(urlObj.url)
    soup = BeautifulSoup(html)

    if HtmlContent.objects.filter(url=urlObj).first() is None:
        english = Language.objects.filter(language_code = "en").first()
        content = HtmlContent.objects.create(language=english,html_source=soup.prettify(),url=urlObj)
        content.save()

    response_data = { 'url' : urlObj.url, 'html': soup.prettify()}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def translate(base_url, text, languageCode):
    url = base_url + "watson/translate"
    payload = "{{\"src\":\"en\",\"dst\":\"{0}\",\"text\":\"{1}\"}}".format(languageCode, text.replace('"', '\\\"')).strip()

    payload = " ".join(payload.split())

    headers = {}
    response = requests.request("POST", url, data=payload, headers=headers)
    response = json.loads(response.text)
    return response['response']

def get_html_from_link(link):
    return urllib.urlopen(link).read()


class HtmlSourceTranslator:
    source = None
    source_lang_code = None
    soup_obj = None

    def __init__(self, html_source, source_lang_code):
        self.source = html_source
        self.source_lang_code = source_lang_code
        self.soup_obj = BeautifulSoup(html_source, 'html.parser')

    def getTextToBeTranslated(self, tag):
        paragraphs_arr = list()
        for paragraph in self.soup_obj.find_all(tag):
            paragraphs_arr.append(paragraph.getText().encode('utf-8').strip())

        return paragraphs_arr

    def createTranslatedHtml(self,  translated_paragraphs, tag):
        translated_soup = BeautifulSoup(self.source, 'html.parser')

        for idx, paragraph in enumerate(translated_soup.find_all(tag)):
            if paragraph.string is None: continue

            paragraph.string.replace_with(translated_paragraphs[idx])
        return translated_soup.prettify()

