from django.shortcuts import render
import requests,json
def index(request):
	print translate("hello")
	return render(request,'home/index.html')


def translate(text):
	url = "http://localhost:8000/watson/translate"

	payload = "{{\"src\":\"en\",\"dst\":\"fr\",\"text\":\"{0}\"}}".format(text)
	print payload
	headers = {}

	response = requests.request("POST", url, data=payload, headers=headers)
	response = json.loads(response.text)

	return response['response']