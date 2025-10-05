import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Read data from the output.json file
    with open(r".\output.json", "r", encoding="utf-8", errors="replace") as f:
     output = json.load(f)
    
    return render_template('index.html', data=output)

@app.route('/api/data')
def api_data():
    # Read data from the output.json file
    with open(r".\output.json", "r", encoding="utf-8", errors="replace") as f:
     output = json.load(f)
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
