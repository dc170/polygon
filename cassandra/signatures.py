#from cassandra.cluster import Cluster
import cassandra
import time
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from sortedcontainers import SortedSet
import yaml
import json

class CassandraDB:

    def __init__(self):
        self._connectDB()
    def __del__(self):
        print self.c.shutdown()

    def _connectDB(self):
        with open("db.yaml", 'r') as stream:
            try:
                data = yaml.load(stream)
                servers = data['malwaredb']['servers']
                user = data['malwaredb']['user']
                passw = data['malwaredb']['pass']
                db = data['malwaredb']['db']

                ap = PlainTextAuthProvider(username=user, password=passw)
                c = Cluster(servers,protocol_version=2, auth_provider=ap)
                self.c = c 
                self.s = c.connect('polygon')
                

            except yaml.YAMLError as exc:
                print(exc)

    def getSignatures(self):
        signatures = {}
        hashes = []
        rows = self.s.execute("select attacker_ip from sql_trap;")
        for r in rows:
            hashes.append(r[0])
        signatures['hashes'] = hashes
        jsignatures = json.dumps(signatures, ensure_ascii=False)
        return jsignatures

            
