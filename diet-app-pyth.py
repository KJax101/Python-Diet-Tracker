from flask import Flask
from flask import request
from flask import render_template
from food_scraper import get_url

# vegetables = get_url(['vegetables'])
vegetables = {
    "carrot": {
        "calories": 60,
        "protein": 2,
        "sugar": 1,
        "name": "carrot"
    }
}
print(vegetables)
app = Flask(__name__)


@app.route("/")
# (ROUTING here) here we are indicating the homepage as /
def hello():
    return render_template("test.html", foods=vegetables, show_results=False)


@app.route("/results", methods=["POST", "GET"])
def login():
    veggies = request.form.getlist('veggie')
    result = 0
    for veg in veggies:
        result += vegetables[veg]['calories']
        # here we append/add the number to the result (which started at 0)
    return render_template("test.html", result=result, show_results=True)


if __name__ == "__main__":
    app.run()
