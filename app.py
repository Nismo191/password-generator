import random
import string
import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/")
def returnPasswordFixedLen():
    passwordObj = generate()
    return passwordObj


@app.route("/<int:length>")
def returnPasswordCustomLen(length):
    passwordObj = generate(length)
    return passwordObj


@app.route("/<int:length>/<string:special>")
def returnPasswordCustomLenCustomSpecial(length, special):
    passwordObj = generate(length, special)
    return passwordObj




def generate(len=10, special="y"):
    password = ""
    
    if special == "y":
        choiceArr = ["num", "char", "special"]
    else:
        choiceArr = ["num", "char"]
    
    for i in range(len):
        choice = random.choice(choiceArr)
        if choice == "char":
            password += random.choice(string.ascii_letters)
        elif choice == "num":
            password += random.choice(string.digits)
        elif choice == "special":
            password += random.choice(["{","}","[","]","(",")","/","'","`","~"","",",";",":",".","<",">"])
        obj = {"password":password, "generated_time": datetime.datetime.now()}
    return obj

