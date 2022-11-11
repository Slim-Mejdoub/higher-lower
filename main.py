from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<int:num>")
def guess(num):
    number = random.randint(0, 9)
    print(number)
    return render_template("guess.html", number=number, num=num)


if __name__ == "__main__":
    app.run(debug=True)