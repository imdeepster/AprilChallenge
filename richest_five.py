#/usr/bin/env python
# This script should read the accounts.json file and print out the five
# wealthiest accounts at the bank, in order from highest to lowest balance.
# Output should take the following form:
# <last name>, <first name>: $<balance>
import json
import re
import pprint as pprint
with open('accounts.json') as jsonfile:
	accounts=[]
	try:
		# I have fixed the errors in the json file using regular expression as I wasn't sure if fixing the errors in json file was to be done programatically or manually.
		# I have also fixed all the bugs in the provided code template
		# The program reads from the json file, fixes errors and sorts the accounts based on the balance in descending order and prints the  wealthiest accounts in the bank in the format mentioned above
		lines=jsonfile.read()
		lines=lines.replace("\'",'"')
		lines=re.sub(r'\":\n','\": {\n',lines)
		lines=re.sub(r'(\w+)\n        "',r'\1,\n        "',lines)
		accounts=json.loads(lines)
		#accounts = json.load(jsonfile)
		#print(accounts)
	except Exception as e:
		print(accounts)
		raise e
accounts_sorted = sorted(accounts, key=lambda accounts : accounts['balance'],reverse=True)
for account in accounts_sorted[:5]:
	print('{0}, {1}: ${2}'.format(account['name']['last'],account['name']['first'],account['balance']))