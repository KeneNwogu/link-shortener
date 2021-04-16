from graphene import ObjectType, String, Schema 
import secrets
from app import app, db
from app.models import Links
import re
# from app.short import Url

class Url:
    def resolve_link(self, info, url):
        code = secrets.token_hex(3)
        host = '127.0.0.1:5000/'
        short_url = host + code

        link = Links.query.filter_by(full_url=url).first()
        if link:
            return link.short_url
        else:
            link = Links(full_url=url, short_url=short_url)
            if link.full_url.find("http://") != 0: 
                link.full_url = "http://" + link.full_url
            db.session.add(link)
            db.session.commit()
            return link.short_url

class ExampleQuery(ObjectType, Url):
    hello = String(name=String(default_value="World"))
    link = String(url=String())

    def resolve_hello(self, info, name):
        return f"Hello {name}"

    # def resolve_link(self, info, url):
    #     link = short_code(url)
    #     return link   

class RootQuery(ExampleQuery, ObjectType):
    pass

schema = Schema(query=RootQuery)
