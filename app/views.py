from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Mondo'  } # Fake user
    posts = [
            {
                'author': { 'nickname': 'John' },
                'body': 'Bela tago cxe San Fransisko!'
                },
            {
                'author': { 'nickname': 'Susan' },
                'body': 'Mi pensas, ke Pitono estas bona.'
                },
            {
                'author': { 'nickname': 'Bob' },
                'body': 'Hodiauxe, my lernis Pitonon kaj GxavaSkripton.'
                },
            {
                'author': { 'nickname': 'Mario' },
                'body': 'Mi sxatas cxi-tiu urbon.'
                },
            ]
    return render_template("index.html",
            title = "Hejmo",
            user = user,
            posts = posts)
