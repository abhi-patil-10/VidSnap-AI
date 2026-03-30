from flask import Flask, render_template,request
import uuid
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'user-uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["GET","POST"])
def create():
    my_id = uuid.uuid1()#returns a unique id in stringformat based on the current time
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        for key , values in request.files.items():
            print(key,values)
            
            file = request.files[key]
            if file :
                filename = secure_filename(file.filename)
                
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],rec_id))     
                file.save(os.path.join(app.config['UPLOAD_FOLDER'] , rec_id,filename))
                
                #capture the description entered by user
                with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id ,"Description.txt") , "w") as file:
                    file.write(desc)
                            
        
            
        
    return render_template("create.html" , my_id = my_id)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)