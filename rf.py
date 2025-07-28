#This is the script that will enumerate subdomains and directories on a website
#Use of this tools should be confined for educational purpose only

import requests
import sys
from urllib.parse import urlparse


def help():
	print('''
	Usage: DOMAIN [options] [v-verbose]
	OPTIONS:
	help - To display this
	subdomain - Enumerate subdomains
	dir - Enumerate hidden directories
	For example
	   python or python3 rf.py google.com subdomain wordlist.txt
	   python or python3 rf.py google.com/RF wordlist.txt
''')
def subdomain():
	payldcnt = 0 
	persis = []
	print(f"Enumerating Subdomains of {basedomain}\n")
	for subdom in dictionary:
		try:
			res = requests.get(f'https://{subdom}.{basedomain}')
		except:
			continue
		payldcnt += 1
		print(f'({payldcnt} of {len(dictionary)}) {subdom}: {res.status_code}-->{res.url}')
		persis.append(subdom)

	print("Subdomain Enumeration Finished",f"\nValid subdomains are -->{persis[0:]}")

def subdir():
	print("Feature not completed yet")
	
if len(sys.argv) < 2 or sys.argv[1].lower()=='help':
	help()
else:
	try:
		url = urlparse(str(sys.argv[2]))
		basedomain = url.path
		option = str(sys.argv[1])
		if option.lower() == "subdomain" or option.lower() == "dir":
			wordlist = str(sys.argv[3])
			with open(wordlist.strip(),'r')as file:
				dictionary = file.read().splitlines()
			if option.lower() == "subdomain":
				subdomain()
			else:
				subdir()
	except IndexError:
		print("Incorrect use of the program\n")
