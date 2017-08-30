import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_recv():
    link = request.args.get('link', '')
    os.system("open %s" % link)
    return 'RECV'
