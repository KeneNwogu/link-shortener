from flask import redirect, url_for
from app import app, db
from app.models import Links

@app.route('/')
def hello():
    return "Hello World"

@app.route("/<code>")
def navigate(code):
    host = "127.0.0.1:5000/"
    url = host + code

    link = Links.query.filter_by(short_url=url).first()
    if link:
        redirect_link = link.full_url
        if redirect_link is not None:
            if redirect_link.find("http://") != 0:
               redirect_link = "http://" + redirect_link
        return redirect(redirect_link)
    else:
        return redirect(url_for('hello'))
    

