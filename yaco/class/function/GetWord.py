import urllib.request
from config import config
import json
def get_word(word):
    APIKEY = config.API_KEY
    palabra = word.replace(' ','%20')
    resp = urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/spanish/json/"+palabra+"?key="+APIKEY).read()
    return json.loads(resp)