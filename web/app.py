from flask import (
    Flask, jsonify, session, redirect, request, Config, render_template
)


app = Flask(__name__)
SECRET_KEY = 'dev key'
DEBUG = True
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
