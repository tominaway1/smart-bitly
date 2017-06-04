import requests
import sys
def get_audio_div(lang,text):
    """
        lang: Pick voice using the Watson abbrevvation for language
        text: Give text to read
    """
    lang_dict={"en":"en-US_MichaelVoice", "es": "es-ES_EnriqueVoice","de":"de-DE_DieterVoice", "fr":"fr-FR_ReneeVoice",
            "it":"it-IT_FrancescaVoice","pt":"pt-BR_IsabelaVoice", "ja":"ja-JP_EmiVoice"}
    lang_string= lang_dict[lang]
    start="<audio id = \"audio\" controls><source id=\"sources\" src=\""
    end= "\" type=\"audio/ogg\"></audio>\""
    html_start="https://3c2fd0a4-fae3-4772-b9a1-01fce49aa56e:f5k3heyKWdJ4@stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio%2Fogg%3Bcodecs%3Dopus&"

    audio_settings= "voice="+lang_string+"&text="+text

    edited_page=start+html_start+audio_settings+end
    return edited_page
#voice=es-ES_EnriqueVoice&text=%20hello
def audio_translate(uuid,lang,text):
    """
    	uuid: unique identifier,
    	lang: english, spanish, german, french, italian, portuguese, japanese
    	text: whatever you want translated, preferably in the language you give
    """
    lang_dict={"english":"en-US_MichaelVoice", "spanish": "es-ES_EnriqueVoice","german":"de-DE_DieterVoice", "french":
    "fr-FR_ReneeVoice", "italian":"it-IT_FrancescaVoice","portuguese":"pt-BR_IsabelaVoice", "japanese":"ja-JP_EmiVoice"}
    lang_string= lang_dict[lang]
    text_string= text
    ogg_file= uuid+".ogg"


    f = open(ogg_file, 'wb')

    #url = "https://watson-api-explorer.mybluemix.net/text-to-speech/api/v1/synthesize"r
    url = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    querystring = {
            "accept":"audio/ogg;codecs=opus",
            "voice": lang_string,
            "text": text_string
        }

    headers = {
        'authorization': "Basic M2MyZmQwYTQtZmFlMy00NzcyLWI5YTEtMDFmY2U0OWFhNTZlOmY1azNoZXlLV2RKNA=="
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    f.write(response.content)
    print "complete"


if __name__== '__main__':
    if len(sys.argv) != 4:
            print "Unexpected Format: python audio_translate.py uuid {english spanish german french italian portuguese japanese} text "
            sys.exit(1)
    uuid= sys.argv[1]
    lang= sys.argv[2]
    text=sys.argv[3]
    #audio_translate(uuid,lang,text)
    print get_audio_div(lang,text)




