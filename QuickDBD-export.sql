-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- tweet
-- ---
-- id int PK
-- tweet varchar
-- user_id int FK - user.user_id
-- date date
-- key_word varchar
-- like varchar
-- retweet int

-- user
-- ---
-- user_id int PK
-- user_name varchar
-- verified BOOL
-- location varchar
-- friends int
-- followers int

-- sentiment
-- ---
-- id int PK FK - tweet.id
-- mood varchar

CREATE TABLE "tweet" (
    "id" int   NOT NULL,
    "tweet" varchar   NOT NULL,
    "user_id" int   NOT NULL,
    "date" date   NOT NULL,
    "key_word" varchar   NOT NULL,
    "like" varchar   NOT NULL,
    "retweet" int   NOT NULL,
    CONSTRAINT "pk_tweet" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "user" (
    "user_id" int   NOT NULL,
    "user_name" varchar   NOT NULL,
    "verified" BOOL   NOT NULL,
    "location" varchar   NOT NULL,
    "friends" int   NOT NULL,
    "followers" int   NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "user_id"
     )
);

CREATE TABLE "sentiment" (
    "id" int   NOT NULL,
    "mood" varchar   NOT NULL,
    CONSTRAINT "pk_sentiment" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "tweet" ADD CONSTRAINT "fk_tweet_user_id" FOREIGN KEY("user_id")
REFERENCES "user" ("user_id");

ALTER TABLE "sentiment" ADD CONSTRAINT "fk_sentiment_id" FOREIGN KEY("id")
REFERENCES "tweet" ("id");

