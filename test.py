from flask import Flask

new = Flask(__name__) #app intialization

@new.route('/profile/<username>')
def  pro_world(username):
    return '<h1>this profile is for %s</h1>' % username


   #app run
new.run()