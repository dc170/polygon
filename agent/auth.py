from flask import Flask
from flask_httpauth import HTTPDigestAuth
import signatures as c

app = Flask(__name__)
app.config['SECRET_KEY'] = '408a5771606748ff56935b5d1da14d2d738d90b8'
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
def index():
    return "polygon signatures update server"

@app.route('/md5')
@auth.login_required
def signatures():
    s = c.CassandraDB()

    return s.getSignatures()

@app.route('/attackers')
@auth.login_required
def ips():
   s = c.CassandraDB()
   return s.getIP()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',ssl_context='adhoc')
