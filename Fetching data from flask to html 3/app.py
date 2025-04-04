from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_heading')
def get_heading():
    return jsonify({"heading": "Hello from Flask!"})  # Sending JSON data

if __name__ == '__main__':
    app.run(debug=True)
