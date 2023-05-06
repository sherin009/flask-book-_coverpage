
from flask import Flask
neww = Flask(__name__) #app intialization

@neww.route('/profile/<int:id>')
def  pro_world(id):
    return '<h1>this profile is for %d</h1>' % id


   #app run
neww.run()