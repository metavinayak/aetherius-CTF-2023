import os

from flask import Flask, make_response, render_template,render_template_string,request
app = Flask(__name__)
@app.route('/')
def home():
    response = make_response("<title>SaSTI website 💉</title><form action='/display' method = 'POST'><h3>Input <br> <input type = 'text' name = 'text' style='width: 80%' autofocus/></p><input type = 'submit' value = 'submit' /></h3></form>")
    return response

@app.route('/display', methods = ["POST"])
def page():
    text = request.form
    try:
        response = make_response(render_template_string(text["text"]))
    except:
        response=make_response("Oops illegal expression")

    return response


app.run(debug = False, host='0.0.0.0', port='5000')
