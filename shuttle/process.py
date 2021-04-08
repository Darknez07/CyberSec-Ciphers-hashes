import ipwhois
from pprint import pprint
file = open('outputofscan.txt','r+')
scan = [f for f in file.read().split('\n') if f!='']
counter = 0
for val in scan:
	if 'Nmap scan report for' in val:
		start = len('Nmap scan report for ')
		take = val[start:].split(' ')
		if len(take) > 1:
			take[-1] = take[-1].strip('(').strip(')')
			obj = ipwhois.IPWhois(take[1])
			try:
				res = obj.lookup_rdap()
				pprint(res['objects'])
			except:
				res = obj.lookup_whois()
				pprint(res)
			finally:
				pas = obj.lookup_whois()
			pprint(pas)
			# break
		counter+=1
print("{} IP's + Domains found".format(counter))
file.close()