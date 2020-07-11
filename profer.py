from flask import Flask, request, render_template
from vkparser import get_subs

app = Flask(__name__)

def category_percent(words):
    pass

def getdic(data):
    name, words = get_subs(str(data))
    print(words)
    probabilities = category_percent(words) # Insert ML here

    name = None
    words = None

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

if __name__ == "__main__":
    app.run(debug=True)