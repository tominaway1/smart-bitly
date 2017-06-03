from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from models import UrlProperties


def index(request):
    return render(request,'home/index.html')

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