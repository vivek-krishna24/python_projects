from flask import Flask, render_template, request
import random

app = Flask(__name__)

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        nr_letters = int(request.form.get("letters", 0))
        nr_symbols = int(request.form.get("symbols", 0))
        nr_numbers = int(request.form.get("numbers", 0))

        pswd = (
            [random.choice(letters) for _ in range(nr_letters)] +
            [random.choice(symbols) for _ in range(nr_symbols)] +
            [random.choice(numbers) for _ in range(nr_numbers)]
        )
        random.shuffle(pswd)
        password = "".join(pswd)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
 
