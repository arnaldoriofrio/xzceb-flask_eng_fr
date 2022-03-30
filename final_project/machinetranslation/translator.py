'''Modulo que traduce de ingles a frances y viceversa '''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(english_text):
    '''Función traduce de ingles a frances'''
    translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text=json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

def frenchToEnglish(french_text):
    '''Función traduce de frances a ingles'''
    translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text=json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text
