from flask import Flask, render_template,request
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["GET","POST"])
def create():
    my_id = uuid.uuid1()
    if request.method == "POST":
        for key , values in request.files.items():
            print(key,values)
    return render_template("create.html" , my_id = my_id)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)