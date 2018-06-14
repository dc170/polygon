#!flask/bin/python
from flask import Flask
import signatures as c

app = Flask(__name__)

@app.route('/md5')
def index():
    s = c.CassandraDB()

    return s.getSignatures()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
