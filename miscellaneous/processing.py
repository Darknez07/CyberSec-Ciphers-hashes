import requests
import json
import subprocess
import pprint
username = input('Enter the github username: ')
url='https://api.github.com/users/'+username+'/repos'
response = requests.get(url)
parsed = json.loads(response.text)
for repo in parsed:
    result = subprocess.run(['bash','cloc-count.sh',repo['clone_url']],stdout=subprocess.PIPE)
    pp = pprint.PrettyPrinter(indent=8)
    print(result.stdout.decode('utf-8'))