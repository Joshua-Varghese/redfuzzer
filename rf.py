#This is the script that will enumerate subdomains and directories on a website
#Use of this tools should be confined for educational purpose only

import requests
import sys
from urllib.parse import urlparse

payldcnt = 0 

def help():
	print('''
	Usage: python3 rf.py domain [options][v-verbose]
	OPTIONS:
	help - To display this
	subdomain - Enumerate subdomains
	dir - Enumerate hidden directories
	For example
''')
def subdomain():
	try:
		persis = []
		print(f"Enumerating Subdomains of {basedomain}\n\n")
		for subdom in dictionary:
			res = requests.get(f'https://{subdom}.{basedomain}')
			global payldcnt
			payldcnt += 1
			print(f'({payldcnt} of {len(dictionary)}): {res.status_code}-->{res.url}')
	except requests.exceptions.ConnectionError:
			print(basedomain)

def subdir():
	pass
	
try:
	url = urlparse(str(sys.argv[1]))
	basedomain = url.path
	print(basedomain)
	option = str(sys.argv[2])
	wordlist = str(sys.argv[3])
		
	with open(wordlist.strip(),'r')as file:
		dictionary = file.read().splitlines()
	 

except IndexError:
	help

subdomain()
