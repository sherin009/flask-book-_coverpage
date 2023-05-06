from flask import Flask

app = Flask(__name__) #app intialization

@app.route('/home')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/')
def hii():
    return '<h2>Hai, are u there?</h2>'

if __name__ == '__main__':   #app run
    app.run()