from flask import Flask,render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:9tckay8Bv^9e@database-2.cfzewqbxonfb.us-east-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)
db.reflect()

# class tweetdb(db.Model):
#     __tablename__ = 'tweet'

# class sentiment(db.Model):
#     __tablename__ = 'sentiment'

# class user(db.Model):
#     __tablename__ = 'user'

@app.route("/")
def index():
    return render_template("index.html")

# Tweet Share
@app.route("/tweet_share")
def tweet_share():
    response = db.session.execute(
            "SELECT tweet.key_word, count(tweet.key_word) FROM tweet WHERE key_word NOT IN ('OLIMPIADAS' )GROUP BY tweet.key_word").fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["total_count"] = i[1]
        dict["key_word"] = i[0]
        tweets.append(dict)
    return jsonify(tweets)

# Twitter Stacked
@app.route("/twitter_stacked")
def twitter_stacked():
    query = '''SELECT tweet.key_word
, SUM(CASE WHEN sentiment.mood < 0.3 THEN 1 ELSE 0 END) AS Negative
, SUM(CASE WHEN sentiment.mood > 0.7 THEN 1 ELSE 0 END) AS Positive
, SUM(CASE WHEN sentiment.mood > 0.3 AND sentiment.mood < 0.7 THEN 1 ELSE 0 END) AS Neutral
FROM tweet LEFT JOIN sentiment ON tweet.id = sentiment.id WHERE tweet.key_word NOT IN ('OLIMPIADAS' )
GROUP BY  tweet.key_word'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["key_word"] = i[0]
        dict["positive"] = i[2]
        dict["negative"] = i[1]
        dict["neutral"] = i[3]
        tweets.append(dict)
    return jsonify(tweets)

# NSAT
@app.route("/nsat")
def nsat():
    query = '''SELECT 
	key_word
, ROUND(AVG(ss.mood)::numeric,2) AS NSAT
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word NOT IN ('OLIMPIADAS')
GROUP BY 1'''

    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["key_word"] = i[0]
        dict["nsat"] = i[1]
        tweets.append(dict)
    return jsonify(tweets)

# Time NSAT
@app.route("/time_nsat")
def time_nsat():
<<<<<<< HEAD
    query = '''SELECT tweet.key_word, CAST(AVG(sentiment.mood)AS FLOAT(2)) , TO_CHAR( tweet.date, 'YYYY-MM') 
FROM tweet LEFT JOIN sentiment ON sentiment.id = tweet.id WHERE tweet.date >= '2021-01-01'
GROUP BY tweet.key_word , tweet.date ORDER BY tweet.date DESC'''
=======
    query = '''SELECT
TO_CHAR(tw.date,'YYYY')
, key_word
, ROUND(AVG(ss.mood)::numeric,2)
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word NOT IN ('OLIMPIADAS')
GROUP BY 1,2 ORDER BY 1 DESC'''
>>>>>>> a3ff3fc33f93934e79b0609ed22bc5d6cb382548
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["key_word"] = i[1]
        dict["nsat"] = i[2]
        dict["year"] = i[0] 
        tweets.append(dict)
    return jsonify(tweets)

# Tree Map
@app.route("/tree_map")
def tree_map():
    query = '''pending'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict[""] = i[0]
        dict[""] = i[1]
        dict[""] = i[1]
        tweets.append(dict)
    return jsonify(tweets)

# Olimpiadas
@app.route("/olimpiadas")
def olimpiadas():
    query = '''SELECT
TO_CHAR(tw.date,'MM')
, ROUND(AVG(ss.mood)::numeric,2) AS NSAT
,COUNT(ss.id) AS total_count
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word = ('OLIMPIADAS') AND TO_CHAR(tw.date,'MM') NOT IN ('04') 
GROUP BY 1 ORDER BY 1 DESC'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["month"] = i[0]
        dict["nsat"] = i[1]
        dict["total_count"] = i[2]
        tweets.append(dict)
    return jsonify(tweets)


if __name__ == "__main__":
    app.run(debug=True)