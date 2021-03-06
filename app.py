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
        dict["nsat"] = float(i[1])
        tweets.append(dict)
    return jsonify(tweets)

# Time NSAT 1
@app.route("/time_nsat")
def time_nsat():
    query = '''SELECT
TO_CHAR(tw.date,'YYYY')
, key_word
, ROUND(AVG(ss.mood)::numeric,2)
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word NOT IN ('OLIMPIADAS')
GROUP BY 1,2 ORDER BY 1 DESC'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["key_word"] = i[1]
        dict["nsat"] = float(i[2])
        dict["year"] = i[0] 
        tweets.append(dict)
    return jsonify(tweets)

# New NSAT 2
@app.route("/nsat2")
def nsat2():
    #PANDEMICS
    query = '''
SELECT
TO_CHAR(tw.date,'YYYY')
, ROUND(AVG(ss.mood)::numeric,2)
, count(tw.id)
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
GROUP BY 1 ORDER BY 1 DESC'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["year"] = i[0]
        dict["nsat"] = float(i[1])
        dict["total_count"] = i[2]
        tweets.append(dict)
    # print(tweets)
    return jsonify(tweets)


# New NSAT 3
@app.route("/nsat3")
def nsat3():
    #blim vs Netflix
    query = '''SELECT
TO_CHAR(tw.date,'YYYY')
, key_word
, ROUND(AVG(ss.mood)::numeric,2)
, count(tw.id)
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word IN ('Blim','Netflix')
AND TO_CHAR(tw.date,'YYYY') IN ('2015','2016','2017') 
GROUP BY 1,2 ORDER BY 1 DESC'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["year"] = i[0]
        dict["key_word"] = i[1]
        dict["nsat"] = float(i[2])
        dict["total_count"] = i[3]
        tweets.append(dict)
    # print(tweets)
    return jsonify(tweets)


# New NSAT 4
@app.route("/nsat4")
def nsat4():
    query = '''SELECT
TO_CHAR(tw.date,'YYYY')
, key_word
, ROUND(AVG(ss.mood)::numeric,2)
, count(tw.id)
FROM tweet tw
LEFT JOIN sentiment ss on tw.id = ss.id
WHERE key_word IN ('Disney')
AND TO_CHAR(tw.date,'YYYY') IN ('2018','2019','2020','2021') 
GROUP BY 1,2 ORDER BY 1 DESC'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["year"] = i[0]
        dict["nsat"] = float(i[2])
        dict["total_count"] = i[3]
        tweets.append(dict)
    # print(tweets)
    return jsonify(tweets)



# Tree Map
@app.route("/tree_map")
def tree_map():
    query = '''SELECT * from word'''
    response = db.session.execute(query).fetchall()
    tweets = []
    for i in response:
        dict = {}
        dict["word"] = i[1]
        dict["count"] = i[2]
        dict["mood"] = i[3]
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
        dict["nsat"] = float(i[1])
        dict["total_count"] = i[2]
        tweets.append(dict)
    # print(tweets)
    return jsonify(tweets)


if __name__ == "__main__":
    app.run(debug=True)