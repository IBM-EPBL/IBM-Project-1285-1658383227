from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'First time using flask \n anush \n arun \n harish \n gowtham'

app.run(host='0.0.0.0', port=81)
