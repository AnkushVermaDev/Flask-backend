from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set Folder Location
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
   
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        # Save File to Specific Folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return f"File '{file.filename}' Uploaded Successfully to '{UPLOAD_FOLDER}' Folder!"

if __name__ == '__main__':
    app.run(debug=True)
