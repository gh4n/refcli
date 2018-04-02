from config import key
import urllib.request

config = key()
key = config.api_key
word = input()
url = "http://words.bighugelabs.com/api/%s/%s/%s/" %(2, key, word)
syns = urllib.request.urlopen(url)
print(syns.read())

