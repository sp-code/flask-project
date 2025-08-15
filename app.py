# save this as app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote'    
    }
]

@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)