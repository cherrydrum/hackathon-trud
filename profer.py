from flask import Flask, request, render_template
from vkparser import get_subs
from machine import category_percent

app = Flask(__name__)

def getdic(data):
    name, words = get_subs(str(data))
    probabilities = category_percent(words)
    return name, probabilities

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    toshow = None
    name = None
    if request.method == 'POST':
        data = request.form['domain']
        if data:
            name, toshow = getdic(data)

    return render_template('index.html', name=name, toshow=toshow)