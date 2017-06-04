from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import text_translate
import audio_translate
@csrf_exempt
def translate(request):
    model = {
        # English <-> French
            "en-fr":"en-fr", "fr-en":"fr-en",
        # French <-> Spanish
            "fr-es":"fr-es","es-fr":"es-fr",
        # English <-> French
            "en-es":"en-es", "es-en":"es-en",
        # English <-> Japanese
            "ja-en":"ja-en", "en-ja":"en-ja",
        # English <-> Arabic, No voice support
           # "ar-en":"ar-en", "en-ar":"en-ar",
        # English <-> German
            "de-en":"de-en", "en-de":"en-de",
        # English <-> Italian
            "it-en":"it-en", "en-it":"en-it",
        # English <-> Portuguese
            "pt-en":"pt-en", "en-pt":"en-pt"
               }
#	lang_dict={"english":"en-US_MichaelVoice", "spanish": "es-ES_EnriqueVoice","german":"de-DE_DieterVoice", "french":
#	"fr-FR_ReneeVoice", "italian":"it-IT_FrancescaVoice","portuguese":"pt-BR_IsabelaVoice", "japanese":"ja-JP_EmiVoice"}

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

def read(request):
    """
        text
        language
        html-page

        Need to insert
        <audio id = "audio" controls>
          <source id="sources" src="https://3c2fd0a4-fae3-4772-b9a1-01fce49aa56e:f5k3heyKWdJ4@stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio%2Fogg%3Bcodecs%3Dopus&voice=es-ES_EnriqueVoice&text=%20hello." type="audio/ogg">
        </audio>
    """
    start="<audio id = \"audio\" controls><source id=\"sources\" src=\""
    end= "\" type=\"audio/ogg\"></audio>\""
    html_start="https://3c2fd0a4-fae3-4772-b9a1-01fce49aa56e:f5k3heyKWdJ4@stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio%2Fogg%3Bcodecs%3Dopus&"
    audio_settings=""
    edited_page=start+html_start+audio_settings+end
    #voice=es-ES_EnriqueVoice&text=%20hello.
    response_data = {
        'sound_page': edited_page
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
