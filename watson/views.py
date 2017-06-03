from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def translate(request):
    model = {}

    model["en-fr"] = "test"

    json_data = None
    if request.method == 'POST':
        json_data = json.loads(request.body)

    src = json_data['src']
    dst = json_data['dst']
    text = json_data['text']

    langString = "{0}-{1}".format(src,dst)

    response_data = {
        'src': src,
        'target': dst,
        'text':text,
        'model_id': model[langString],
        'translation':"yo what da fuck"
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

