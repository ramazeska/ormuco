from flask import render_template, request
from flask import current_app as app
from .models import db, Pets
from sqlalchemy import exc


@app.route("/")
def home():
    title = "Test assignment"
    try:
        return render_template("index.html", title=title, mode='root')
    except Exception as e:
        return str(e)


@app.route("/validate")
def validate():
    items = request.args
    name = items.get('name', type=str)
    color = items.get('color', type=str)
    pet = items.get('pet', type=str)

    if validate_str(name) is False or validate_str(color) is False or validate_str(pet) is False:
        return render_template("index.html", mode='validate', name=name, color=color, pet=pet)
    if pet.lower() not in ['dog', 'cat']:
        return render_template("index.html", mode="validatepet", pet=pet)

    else:
        # try to create entry
        new = Pets()
        new.pet = pet
        new.color = color
        new.name = name
        try:
            db.session.add(new)
            db.session.commit()
        except exc.IntegrityError:
            return render_template("index.html", mode="exists")
        except Exception as e:
            raise e

        return render_template("index.html", mode='submitted', values=Pets.query.filter_by(name=name).all())  # here - add sql db table


def validate_str(item):
    if any(char.isdigit() for char in item) is True:
        return False
    return True

