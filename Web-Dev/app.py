from search import generate_recipe
from flask import Flask, redirect, render_template, url_for, request
from database import db, Recipe, Bookmark
import json

# def generate_recipe(query): \\test i used
#     return {
#         "url": f"https://example.com/{query.replace(' ', '-').lower()}",
#         "name": f"{query.title()}",
#         "author": "Test Generator",
#         "source": "Local Placeholder",
#         "rating": 5.0,
#         "reviews": 1,
#         "prepT": "15 min",
#         "cookT": "45 min",
#         "totalT": "1 hr",
#         "servings": "8",
#         "calories": "320",
#         "category": "Dessert",
#         "cuisine": "American",
#         "description": f"A sample recipe generated for {query}.",
#         "ingredients": json.dumps([
#             "2 apples",
#             "1 pie crust",
#             "1/2 cup sugar",
#             "1 tsp cinnamon"
#         ]),
#         "Note: "This is placeholder data."
#     }



app = Flask(__name__)

#database creation
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def Home():
    return redirect (url_for('about'))
#     # return render_template("search.html");


@app.route("/about/")
def about():
    return render_template("about.html");

@app.route("/search/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if not query:
            return render_template("search.html", error="Please enter a search term.")
        recipe_data = generate_recipe(query)
        return render_template("recipes.html", recipe=recipe_data)
    return render_template("search.html")

@app.route("/save/", methods=["POST"])
def save_recipe():
    try:
        existing_recipe = Recipe.query.filter_by(url=request.form.get("url")).first()

        if existing_recipe:
            return redirect(url_for("saved"))
        
        recipe = Recipe(
            url=request.form.get("url"),
            name=request.form.get("name"),
            author=request.form.get("author"),
            source=request.form.get("source"),
            rating=float(request.form.get("rating", 0)),
            reviews=int(request.form.get("reviews", 0)),
            prepT=request.form.get("prepT"),
            cookT=request.form.get("cookT"),
            totalT=request.form.get("totalT"),
            servings=request.form.get("servings"),
            calories=request.form.get("calories"),
            category=request.form.get("category"),
            cuisine=request.form.get("cuisine"),
            description=request.form.get("description"),
            ingredients=request.form.get("ingredients"),
            notes=request.form.get("notes")
        )

        db.session.add(recipe)
        db.session.commit()

        return redirect(url_for("saved"))

    except Exception as e:
        return f"Error saving recipe: {e}", 500

# @app.route("/recipies/")
# def recipie():
#     return render_template("recipies.html");

@app.route("/saved/")
def saved():
    recipes = Recipe.query.all()
    return render_template("saved.html", recipes=recipes)

# @app.route("/search/")
# def search():
#     return render_template("search.html");

@app.route("/delete/<int:recipe_id>/", methods=["POST"])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("saved"))

if __name__ == "__main__":
    print("[}----------- [Running app.py] ---------------{]")
    app.run(debug=True)