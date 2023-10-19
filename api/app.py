from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def zodiac_sign(day, month):
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    return astro_sign

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_birthdate = request.form.get("birthdate")

    birthdate = datetime.strptime(birthdate, "%d-%m-%y")
    zodiac = zodiac_sign(birthdate.day, birthdate.month)

    return render_template("hello.html", name=input_name, birthdate=input_birthdate>

