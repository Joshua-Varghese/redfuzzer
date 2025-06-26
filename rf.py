#This is the script that will enumerate subdomains and directories on a website
#Use of this tools should be confined for educational purpose only

import requests
import sys
from urllib.parse import urlparse

def help():
	print('''
	Usage: python3 rf.py domain [options][v-verbose]
	OPTIONS:
	help - To display this
	subdomain - Enumerate subdomains
	dir - Enumerate hidden directories
	For example
''')
try:
	url = sys.argv[1]
	option = sys.argv[2]
	wordlist = sys.argv[3]
	verbose = sys.argv[4]

	def subdomain(url,wordlist):
		try:
			dictionary = open(wordlist.strip(),'r').splitlines()
			persis = []
			print(f"Enumerating Subdomains of {url}\n\n")
			for subdom in dictionary:
				res = requests.get(f"http://{subdom}.{urlparse(url.strip())}")
				if res.raise_for_status != None:
					print(f'{res.url}:{res.status_code}')
				else:
					print(f'{res.url}:Valid')	
					persis.append(res.url)
				if(verbose):
					print(f'Returned {str(res.status_code))} for {res.url}')				
			
			except ConnectionError:
				print("Unable to probe, Check your Internet Connectivity")
			

