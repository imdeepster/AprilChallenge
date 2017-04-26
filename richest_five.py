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