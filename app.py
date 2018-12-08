from flask import Flask
from flask import request
from flask import render_template
import numpy as np

# from routes import app_initializer


# initialize the app
app = Flask(__name__)
# __name__ built into Python, grabbing the name of the main file

# creating app routes

# calories, Fat, carbs, protein, sugars]
# using Numpy array in order to make calculations easier, instead of doing a for-loop
foods = {"carrot": np.array([60, 0, 58, 1, 1]),
         "tomato": np.array([55, 0, 54, 1, 1]),
         "eggs": np.array([65, 3, 50, 15, 2]),
         "american cheese": np.array([90, 5, 80, 10, 3]),
         "turkey": np.array([90, 5, 50, 18, 3])}


@app.route("/")
def displayPage():
    return render_template("index.html")


def calorieCalculator(foods):
    pass


@app.route("/result", methods=["GET", "POST"])
def formDataInput():
    form = request.form
    print(form)
    return "form"


# now we run the app
if __name__ == "__main__":
    app.run()
