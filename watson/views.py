from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import text_translate
@csrf_exempt
def translate(request):
    model = {
        # English <-> French
            "en-fr":"en-fr", "fr-en":"fr-en",
        # French <-> Spanish
            "fr-es":"fr-es","es-fr":"es-fr",
        # English <-> French
            "en-es":"en-es", "es-en":"es-en"
        }

    json_data = None
    if request.method == 'POST':
        json_data = json.loads(request.body)

    src = json_data['src']
    dst = json_data['dst']
    text = json_data['text']

    langString = "{0}-{1}".format(src,dst)
    model_id=model[langString] if model[langString] else None
    translation=text_translate.translate(model_id, text)
    response_data = {
        'response': translation
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

