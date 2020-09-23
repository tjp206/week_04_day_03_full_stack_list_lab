from flask import Flask, render_template

from models.animals import Animals

from flask import Blueprint

from repositories import animals_repo

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals") # setting a route
def animals():
    animals = animals_repo.select_all()
    return render_template("animals/index.html", all_animals=animals)
