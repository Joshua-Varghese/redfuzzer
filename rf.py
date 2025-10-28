'''
This is the script that will enumerate subdomains and directories on a website.
Always keep in mind that all the request you sent using this script are logged network log
of the target server or computer. Be responsible with the use.
'''

import requests
import sys
from urllib.parse import urlparse
from urlfilter import filter_domain

global option
#Help function
def seekhelp():
	print('''
	Usage: DOMAIN [options]
	OPTIONS:
	help - To display this
	subdomain - Enumerate subdomains
	dir - Enumerate hidden directories
	For example
	   python or python3 rf.py https://google.com subdomain wordlist.txt
	   python or python3 rf.py https://google.com/RF dir wordlist.txt
''')
print
(r"""
.%%%%%...%%%%%%..%%%%%...%%%%%%..%%..%%..%%%%%%..%%%%%%..%%%%%%..%%%%%..
.%%..%%..%%......%%..%%..%%......%%..%%.....%%......%%...%%......%%..%%.
.%%%%%...%%%%....%%..%%..%%%%....%%..%%....%%......%%....%%%%....%%%%%..
.%%..%%..%%......%%..%%..%%......%%..%%...%%......%%.....%%......%%..%%.
.%%..%%..%%%%%%..%%%%%...%%.......%%%%...%%%%%%..%%%%%%..%%%%%%..%%..%%.
........................................................................

""")


#Function to enumerate subdomains.
def subdomain():

	persis = []
	payldcnt = 0 

	print(f"Enumerating Subdomains of {basedomain}\n")
	for subdom in dictionary:
		try:
			res = requests.get(f'{connection_scheme}://{subdom}.{basedomain}')
		except:
			continue
		payldcnt += 1
		print(f'({payldcnt} of {len(dictionary)}) {subdom}: {res.status_code}-->{res.url}')
		persis.append(subdom)

	print("Subdomain Enumeration Finished",f"\nValid subdomains are -->{persis[0:]}")

#Function to FUZZ hidden directories
def subdir():
	dir_persis = []
	dir_payload_cnt = 0

	print(f"Fuzzing Directories of {basedomain}\n")
	for subdir in dictionary:
		try:
			res = requests.get(f'{connection_scheme}://{basedomain}/{subdir}')
		except:
			continue
		dir_payload_cnt += 1
		print(f'({dir_payload_cnt} of {len(dictionary)}) {basedomain}: {res.status_code}-->{res.url}')
		if res.status_code == 200:
			dir_persis.append(subdir)

	print("Subdirectory Fuzzing Finished",f"\nValid Subdirectories are -->{dir_persis[0:]}")

if len(sys.argv) < 2 or sys.argv[1].lower()=='help':
	seekhelp()
else:
	try:
		url = urlparse(str(sys.argv[1])) # Get the url
		option = str(sys.argv[2]) # Help, subdomain or dir fuzzing
		wordlist = str(sys.argv[3]) # Handle wordlist
		basedomain = filter_domain(url.netloc) #Suppose to return a url without the www. in it, if its www.google.com it returns google.com
		connection_scheme = url.scheme
		#dirfuzz = url.path
		#print(dirfuzz)
	except IndexError:
		print("Incorrect use of the program")
		seekhelp()


if option.lower() == "subdomain" or option.lower() == "dir":

	with open(wordlist.strip(),'r')as file:
		dictionary = file.read().splitlines()
	if option.lower() == "subdomain":
		subdomain()
	else:
		subdir()


