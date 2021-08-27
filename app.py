from flask import Flask,render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:9tckay8Bv^9e@database-2.cfzewqbxonfb.us-east-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)
db.reflect()

class tweetdb(db.Model):
    __tablename__ = 'tweet'

class sentiment(db.Model):
    __tablename__ = 'sentiment'

class user(db.Model):
    __tablename__ = 'user'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tweet_share")
def tweet_share():
    response = tweetdb.query.all()
    tweets = []
    for i in response:
        dict = {}
        dict["tweet"] = i.tweet
        dict["key_word"] = i.key_word
        tweets.append(dict)
    return jsonify(dict)

if __name__ == "__main__":
    app.run(debug=True)