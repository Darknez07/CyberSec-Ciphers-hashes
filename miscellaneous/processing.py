import requests
import json
import subprocess
import pprint
username = input('Enter the github username: ')
url='https://api.github.com/users/'+username+'/repos'
response = requests.get(url)
parsed = json.loads(response.text)
check = 0
languages = dict()
for repo in parsed:
	result = subprocess.run(['bash','cloc-count.sh',repo['clone_url']],stdout=subprocess.PIPE)
	pp = pprint.PrettyPrinter(indent=8)
	see = result.stdout.decode('utf-8').split('\n')
	for i in range(11,len(see)):
		lst = []
		for j in see[i].split(" "):
			if j.startswith('-'):
				continue
			if j!='':
				lst.append(j)
		if lst == []:
			continue
		try:
			languages[lst[0]]+=int(lst[-1])
		except:
			languages[lst[0]] = int(lst[-1])
		check+=1
		if check == 8:
			break
print(languages)