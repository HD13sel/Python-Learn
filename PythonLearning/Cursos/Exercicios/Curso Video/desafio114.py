import urllib
import urllib.request
try:
    url = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mNão consegui acessar o site!\033[m')
else:
    print('\033[32mConsegui acessar o site!\033[m')
