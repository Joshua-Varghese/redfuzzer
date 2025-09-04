#This is the script that will enumerate subdomains and directories on a website
#Use of this tools should be confined for educational purpose only

import requests
import sys
from urllib.parse import urlparse

#Help function
def help():
	print('''
	Usage: DOMAIN [options]
	OPTIONS:
	help - To display this
	subdomain - Enumerate subdomains
	dir - Enumerate hidden directories
	For example
	   python or python3 rf.py https://google.com subdomain wordlist.txt
	   python or python3 rf.py https://google.com/RF/about dir wordlist.txt
''')

def filter_domain(bd):
	filter_bd = bd.split(".")
	if filter_bd[0] == "www":
		del filter_bd[0]
	return ".".join(filter_bd)

#Function to enumerate subdomains.
def subdomain():

	persis = []
	payldcnt = 0 

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

#Function to FUZZ hidden directories
def subdir():
	print("Feature not completed yet")
	

if len(sys.argv) < 2 or sys.argv[1].lower()=='help':
	help()
else:
	try:
		url = urlparse(str(sys.argv[1])) # Get the url
		option = str(sys.argv[2]) # Help, subdomain or dir fuzzing
		wordlist = str(sys.argv[3]) # Handle wordlist
		basedomain = filter_domain(url.netloc) #Suppose to return a url without the www. in it
		print(basedomain)
		dirfuzz = url.path
		if option.lower() == "subdomain" or option.lower() == "dir":

			with open(wordlist.strip(),'r')as file:
				dictionary = file.read().splitlines()
			if option.lower() == "subdomain":
				subdomain()
			else:
				subdir()
	except IndexError:
		print("Incorrect use of the program")
		help()

