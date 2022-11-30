
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    """
    This function translates passed English text to French 
    """
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    # frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    frenchText = translation['translations'][0]['translation']
    return frenchText



if __name__ == "__main__":
    print(englishToFrench('Hello, my name is Anon'))