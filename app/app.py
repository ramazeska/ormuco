#/usr/bin/env python3

from flask import Flask, render_template, request
#import re

app = Flask(__name__)
"""TODO
1. create bootstrap frontpage : done
2. redirect to input valiidation - if failed - display error - otherwise return page with "submitted ok": done
2. add sql alchemy
3. add mysql db via 2
4. add config to run flask via gunicorn
5. check via aws - ssl / create self signed certificate
6. check how to add fw + lb with ssl termination on aws 
7. create ansible job to setup all on aws instance
7.1 add  "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDftZwLvh3prVYPxD01zBpehPA6NVlL+iDajlDR2PqzB3odo5gVrV+u6vTyw/TfFR70uOkzoLjxl6x7ZbwXpKBAXqD8ke8gIDOAL4wz8QSKtj1lcLiLOEW0ToKhlwHvlZnA0e/GATtCgt/2y4F+h+jG0VmO3Ae+8aayCOSPVHqKhXcdKt5Qa++/7SuUrTuBN6ApJNp7HmVbMGdSbrr4I1gxNDYONompBTwVvBswBy8ySA+BNaAnKUxsX5gJJCtNENcbtg44TMHufmn69XZeUajDtNGeOgeITAIWnuEiOY+3R70idXJZGSDRnZzs4sXYmP7k4PQq07sWuHqXVKUzYWI/ test"
to aws instance, add my key 
8. test
"""

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

    return render_template("index.html", mode='submitted')  # here - add sql db table

def validate_str(item):
    if any(char.isdigit() for char in item) is True:
        return False
    return True





if __name__ == "__main__":
    app.run(debug=True)