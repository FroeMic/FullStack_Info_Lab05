from flask import Flask
from flask import redirect
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hey there</h1>'

@app.route('/hello2')
def hello2():
    return '<h1>Hey there 2</h1>'

@app.route('/google')
def google():
    return redirect('https://www.google.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hey there, %s</h1>' % name

@app.route('/response_object')
def response_object():
    response = make_response('<h1>I give you cookies</h1>')
    response.set_cookie('Flask', 'is_cool')
    return response

@app.route('/jinja')
def jinja():
    return render_template('index.html')

@app.route('/jinja/<name>')
def jinjad(name):
    d = {
        'key': 'value'
    }
    l = ['a','b','c']
    class myObj:
        def someMethod(self):
            return "Hi there. I am a class."
    return render_template('index_2.html', name=name, d=d, l=l, o=myObj())

@app.route('/template')
def template():
    return render_template('extend.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
