from flask import Flask, jsonify, render_template
from flask_cors import CORS
import logging

# instantiate the app
# Frontend側で生成した画面をBackend側で表示するようにする
app = Flask(__name__, static_folder='./dist/static', template_folder='./dist') 
#app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# LEVEL を DEBUG に変更
logging.basicConfig(level=logging.DEBUG)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=('GET', 'POST'))
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run()