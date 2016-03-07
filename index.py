from flask import Flask
from time import strftime
app = Flask(__name__)


@app.route('/')
def time():
    return strftime('%d/%m/%Y %H:%M:%S')

if __name__ == '__main__':
    app.run()

