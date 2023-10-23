from flask import Flask, render_template, request

app = Flask(__name__)


def zodiac_sign(month):
    if month == 12:
        astro_sign = "Sagittarius"
    elif month == 1:
        astro_sign = "Capricorn"
    elif month == 2:
        astro_sign = "Aquarius"
    elif month == 3:
        astro_sign = "Pisces"
    elif month == 4:
        astro_sign = "Aries"
    elif month == 5:
        astro_sign = "Taurus"
    elif month == 6:
        astro_sign = "Gemini"
    elif month == 7:
        astro_sign = "Cancer"
    elif month == 8:
        astro_sign = "Leo"
    elif month == 9:
        astro_sign = "Virgo"
    elif month == 10:
        astro_sign = "Libra"
    elif month == 11:
        astro_sign = "Scorpio"
    return astro_sign


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_month = int(request.form.get("month"))

    zodiac = zodiac_sign(input_month)

    return render_template(
        "hello.html", name=input_name, month=input_month, zodiac=zodiac
    )
