import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com')

def englishtofrench(word):
    """This class does english to french translation"""

    url_lt='https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/2a3eccb3-7045-4e6d-b92f-99be8d2d2b39'
    apikey_lt='0pro7WArz2p7CypDRzsfwIsZAm5N8K5A8QtWEazubfpj'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    """This class does french to english translation"""

    url_lt='https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/2a3eccb3-7045-4e6d-b92f-99be8d2d2b39'
    apikey_lt='0pro7WArz2p7CypDRzsfwIsZAm5N8K5A8QtWEazubfpj'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']
