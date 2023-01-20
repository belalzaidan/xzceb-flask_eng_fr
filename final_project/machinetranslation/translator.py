import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

"""
   Class to handle language translation using IBM Watson Language Translator
"""
       
apikey = 'YSDRictBUklgYf4JLtyWK81i-jcu1EUwSaPbmRSwqLj9'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b085f3c3-43b5-482e-b2ea-2fbe71ab6661'
language_translator.set_service_url(url)

languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))


def englishToFrench(englishText):
    frenchText = language_translator.translate(text = englishText, model_id = 'en-fr').get_result()
    return frenchText.get("translations")[0]["translatedText"]


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text = frenchText, model_id = 'fr-en').get_result()
    return englishText.get("translations")[0]["translatedText"]