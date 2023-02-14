# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the database URI in the Flask configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/database'

# Create an instance of the SQLAlchemy class and pass it the app object
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fridge_items = db.relationship('FridgeItem', backref='user', lazy=True)
    recipes = db.relationship('Recipe', backref='user', lazy=True)

# Define the FridgeItem model
class FridgeItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Define the Ingredient model as a subclass of the FridgeItem model
class Ingredient(FridgeItem):
    __mapper_args__ = {'polymorphic_identity': 'ingredient'}

# Define the RecipeIngredient model
class RecipeIngredient(db.Model):
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(255), nullable=False)
   
