from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from app.schema import schema
app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

from app import routes
