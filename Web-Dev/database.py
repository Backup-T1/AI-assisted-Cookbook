from flask_sqlalchemy import SQLAlchemy 

# from sqlalchemy import create_engine;
# from sqlalchemy.orm import declarative_base
t = True
f = False
db = SQLAlchemy()
# Integer = db.Integer 
# # db.String = db.String(100)
# Float = db.Float
# Base = declarative_base()
# engine = create_engine("sqlite:///instance/recipies.sqlite")

#Stuck to one here for demo, also Collumn didnt work and so I changed to Column

class Bookmark(db.Model):
    __tablename__ = "Bookmarks"
    id          = db.Column(db.Integer, primary_key = t)
    url         = db.Column(db.String(500), unique = t, nullable = f)
    name        = db.Column(db.String(100), nullable = f)
    author      = db.Column(db.String(100), nullable = f)
    source      = db.Column(db.String(100), nullable = f)
    rating      = db.Column(db.Float, nullable = f)
    reviews     = db.Column(db.Integer, nullable = f)


class Recipe(db.Model):
    __tablename__= "Recipes"
    id          = db.Column(db.Integer, primary_key = t)
    url         = db.Column(db.String(500), unique = t, nullable = f)
    name        = db.Column(db.String(100), nullable = f)
    author      = db.Column(db.String(100), nullable = f)
    source      = db.Column(db.String(100), nullable = f)
    rating      = db.Column(db.Float, nullable = f)
    reviews     = db.Column(db.Integer, nullable = f)
    prepT       = db.Column(db.String(100), nullable = f)
    cookT       = db.Column(db.String(100), nullable = f)
    totalT      = db.Column(db.String(100), nullable = f)
    servings    = db.Column(db.String(100), nullable = f)
    calories    = db.Column(db.String(100), nullable = f)
    category    = db.Column(db.String(100), nullable = f)
    cuisine     = db.Column(db.String(100), nullable = f)
    description = db.Column(db.String(1000), nullable = f)
    ingredients = db.Column(db.Text, nullable = f)
    notes       = db.Column(db.String(1000), nullable = f)

    