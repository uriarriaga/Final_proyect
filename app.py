from flask import Flask,render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:9tckay8Bv^9e@database-2.cfzewqbxonfb.us-east-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tweet_share")
def tweet_share():
    response = [
    {
        "key_word": "Netflix",
        "total_count": 700000
    },
    {
        "key_word": "Amazon Prime Video",
        "total_count": 300000
    },
    {
        "key_word": "HBO Max",
        "total_count": 100000
    },
    {
        "key_word": "Paramount+",
        "total_count": 50000
    },
    {
        "key_word": "Blim",
        "total_count": 350000
    },
    {
        "key_word": "Star Plus",
        "total_count": 10000
    },
    {
        "key_word": "Disney +",
        "total_count": 500000
    }
]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)