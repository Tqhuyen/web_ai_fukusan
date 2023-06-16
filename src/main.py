import flask
from flask import request, render_template, Flask
from flask_cors import CORS
from predict import predict
import os
import glob
import shutil

curent_path=  str(os.path.abspath(os.getcwd()))
print(curent_path)
app = Flask("web AI", static_url_path="/static")
UPLOAD_FOLDER = str(os.path.join("static", "data"))

CORS(app)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def process():
    image = request.files["file"]
    if image:
        name = image.filename
    file_dir =os.path.join(curent_path, UPLOAD_FOLDER, f"{name}")
    image.save(file_dir)
    
    res = predict(file_dir)
    image_dir = glob.glob("E:\\Learn\\web_ai\\runs\\detect\\predict\\*")
    image_dir.sort()
    shutil.copyfile(image_dir[0], file_dir)
    shutil.rmtree(image_dir[0])
    return render_template("index.html", file=file_dir, text_result=str(res[0].names))
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8001)
