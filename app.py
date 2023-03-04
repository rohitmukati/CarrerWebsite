from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id':1,
        'title': 'Software Developer',
        'location': "Indore, india",
        'budget': 'Rs. 15,00,000'
        
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': "Bengulure, india",
        'budget': 'Rs. 30,00,000'
    },
    {
        'id':3,
        'title': 'Frontend Engineer',
        'location': "Mumbai, india",
        'budget':'Rs. 25,00,000'
        
    },
    {
        'id':4,
        'title': 'Backend Engineer',
        'location': "San Francisco, india",
        'budget': 'Rs. 30,00,000'
    }
]

@app.route("/")
def hello_Rohit():
    return render_template('home.html',
                           jobs=JOBS, company_name='IT Park')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
