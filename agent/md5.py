import json
import sqlite3
from subprocess import call
import requests
from requests.auth import HTTPDigestAuth
response = requests.get('http://185.86.149.89:5000/md5',auth=HTTPDigestAuth('john', 'hello'))
res =  response.json()

ips = res['hashes']


conn = sqlite3.connect('signatures.sqlite')
c = conn.cursor()
for ip in ips:
	#print ip
	query = "INSERT INTO binaries (md5) VALUES ('%s')" % (ip)
	#print query
	print "Updating the local database with: " + ip
	c.execute(query)
	conn.commit()

conn.close()