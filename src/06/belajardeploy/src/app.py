from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world from teknik pemrograman 2019-07-11'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
