from flask import Flask
import json

a = '{"name":"hello","end":"world!"}'

app = Flask(__name__)

@app.route("/")



def hello():
    y = json.loads(a)
    z = y["name"] + ' ' + y["end"]
    return z

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
