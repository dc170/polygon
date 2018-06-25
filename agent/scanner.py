import json
import sqlite3
from subprocess import call
import requests
from requests.auth import HTTPDigestAuth
import os
import sys
import hashlib





def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def checkBinary(hash):
    conn = sqlite3.connect('signatures.sqlite')
    c = conn.cursor()
    query = "select md5 from binaries where md5 is '%s'" % (hash)
    res = c.execute(query)
    res = res.fetchone()
    if res is None:
        return False
    else:
        return True
    conn.close()

for dirpath, dirs, files in os.walk("./test/"):	
	for filename in files:
		fname = os.path.join(dirpath,filename)
	try:
            print md5(fname)
            if checkBinary(md5(fname)):
                print "VIRUS DETECTED: " + fname
        except:
            print "error loading file"
