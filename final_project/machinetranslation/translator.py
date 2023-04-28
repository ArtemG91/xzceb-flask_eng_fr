''' This module request provides en-fr and fr-en traslations.'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-28',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''This function provides en-fr translation.'''
    response = language_translator.translate(
	    text=english_text, model_id='en-fr').get_result()
    french_text = response["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    '''This function provides fr-en translation.'''
    response = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = response["translations"][0]["translation"]
    return english_text

if __name__=='__main__':
    out = english_to_french("Hello")
    print(out)
