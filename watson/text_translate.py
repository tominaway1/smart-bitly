import requests
import sys
def translate(model_id,text):
	"""
		model-id: source to final translation given by ibm model id get request,
		text: whatever you want translated, preferably in the language you give

		** Security is currently just hardcoded, we need to fix this eventually **
	"""

        url = "https://gateway.watsonplatform.net/language-translator/api/v2/translate"
	querystring = {"model_id":model_id,
	"text":text}

	headers = {
	    'authorization': "Basic ODVhY2VkNGQtNTYwZS00YjZhLTk3ZjctY2RkZGE4YWU1YjBmOlMxNUpmNk5peWNqWA==",
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)
	return response.text
if __name__== '__main__':
	#currently assumes languages are correct
	if len(sys.argv) != 3:
		print "Unexpected Format"
		sys.exit(1)
	model_id= sys.argv[1]

	text=sys.argv[2]
	translate(model_id,text)




