from flask import Flask, render_template

appy=Flask(__name__)


@appy.route('/')
def index():
    return render_template('index.html')
@appy.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=False)

@appy.route('/books')
def book():
    books=[{'name':'book1','author':'abc',"cover":'https://images.pexels.com/photos/256450/pexels-photo-256450.jpeg?auto=compress&cs=tinysrgb&w=600'},{'name':'book2','author':'tftft',"cover":'https://images.pexels.com/photos/256450/pexels-photo-256450.jpeg?auto=compress&cs=tinysrgb&w=600'},{'name':'book3','author':'ju',"cover":'https://images.pexels.com/photos/256450/pexels-photo-256450.jpeg?auto=compress&cs=tinysrgb&w=600'}]
    return render_template('book.html',books=books)
appy.run(debug=True)

