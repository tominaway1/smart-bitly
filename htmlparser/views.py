from django.http import HttpResponse
from django.shortcuts import render
import requests,json,urllib
from django.views.decorators.csrf import csrf_exempt
from models import UrlProperties, HtmlContent
from watson.models import Language
from urlparse import urlparse
from uuid import UUID
from bs4 import BeautifulSoup


def index(request):
    parsed_uri = urlparse(request.build_absolute_uri())
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    print translate(domain, "hello")
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

    print response_data

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def read_url(request,uuid):
    urlObj = UrlProperties.objects.filter(uuid = UUID(uuid).hex).first()

    html = get_html_from_link(urlObj.url)
    soup = BeautifulSoup(html)

    if HtmlContent.objects.filter(url=urlObj).first() is None:
        english = Language.objects.filter(language_code = "en").first()
        content = HtmlContent.objects.create(language=english,html_source=soup.prettify(),url=urlObj)
        content.save()
        
    response_data = { 'url' : urlObj.url, 'html': soup.prettify()}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def translate(base_url, text):
    url = base_url + "watson/translate"
    payload = "{{\"src\":\"en\",\"dst\":\"fr\",\"text\":\"{0}\"}}".format(text)
    headers = {}
    response = requests.request("POST", url, data=payload, headers=headers)
    response = json.loads(response.text)
    return response['response']

def get_html_from_link(link):
    return urllib.urlopen(link).read()