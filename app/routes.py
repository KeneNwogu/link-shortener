import secrets
from flask import redirect, url_for, render_template, request
from app import app, db
from app.forms import UrlForm
from app.models import Links

@app.route('/', methods=['GET', 'POST'])
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    form = UrlForm()
    if form.validate_on_submit():
        url = form.url.data
        host = request.host
        print(host)
        link = Links.query.filter_by(full_url=url).first()
        if link:
            return render_template('generate.html', short_link=link.short_url)
        else:
            code = secrets.token_hex(3)
            short_url = host + '/' + code
            link = Links(full_url=url, short_url=short_url)
            db.session.add(link)
            db.session.commit()
            return render_template('generate.html', form=form, short_link=short_url)
    return render_template('generate.html', form=form)

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
        return redirect(url_for('generate'))
    

