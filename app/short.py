from app.models import Links
from app import db, app
import secrets

example_urls = ['www.google.com', 'www.instagram.com', 'www.twitter.com']

class Url:
    def resolve_link(url):
        code = secrets.token_hex(3)
        host = '127.0.0.1:5000/'
        short_url = host + code
        with app.app_context():
            link = Links.query.filter_by(full_url=url).first()
        if link:
            return link.short_url
        else:
            with app.app_context():
                link = Links(full_url=url, short_url=short_url)
                db.session.add(link)
                db.session.commit()
            return link.short_url
