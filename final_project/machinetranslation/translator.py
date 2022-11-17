"""Translator EN/FR and FR/EN"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2022-11-17'

"""Create instance of translator."""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englisth_to_french(english_text):
    """Function to translate from English to French."""
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """Function to translate from French to English."""
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
