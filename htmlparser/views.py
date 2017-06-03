from django.http import HttpResponse
from django.shortcuts import render
import requests,json
from django.views.decorators.csrf import csrf_exempt
from models import UrlProperties
from urlparse import urlparse

@csrf_exempt
def create_url(request):
    url = None
    if request.method == 'POST':
        url = request.POST.get("url", "")

    urlObj = UrlProperties.objects.create()
    urlObj.url = url;
    urlObj.save()
    response_data = { 'url' : str(urlObj.uuid) }

    print response_data

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def index(request):

    parsed_uri = urlparse(request.build_absolute_uri())
    print parsed_uri
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    print domain
    print translate(domain, "hello")
    return render(request,'home/index.html')


def translate(base_url, text):
	url = base_url + "watson/translate"

	payload = "{{\"src\":\"en\",\"dst\":\"fr\",\"text\":\"{0}\"}}".format(text)
	print payload
	headers = {}

	response = requests.request("POST", url, data=payload, headers=headers)
	response = json.loads(response.text)

	return response['response']