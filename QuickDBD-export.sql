-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- tweet
-- ---
-- id int PK
-- text varchar
-- user varchar FK - user.id
-- time date
-- ticker varchar FK - ticker.id
-- mood varchar
-- likes int
-- rts int

-- user
-- ---
-- id int PK
-- name varchar
-- verified BOOL
-- location varchar
-- followings int
-- followers int

-- ticker
-- ---
-- id int PK
-- name varchar
-- open DOUBLE 
-- close DOUBLE




CREATE TABLE "tweet" (
    "id" int   NOT NULL,
    "text" varchar   NOT NULL,
    "user" varchar   NOT NULL,
    "time" date   NOT NULL,
    "ticker" varchar   NOT NULL,
    "mood" varchar   NOT NULL,
    "likes" int   NOT NULL,
    "rts" int   NOT NULL,
    CONSTRAINT "pk_tweet" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "user" (
    "id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "verified" BOOL   NOT NULL,
    "location" varchar   NOT NULL,
    "followings" int   NOT NULL,
    "followers" int   NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "ticker" (
    "id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "open" DOUBLE   NOT NULL,
    "close" DOUBLE   NOT NULL,
    CONSTRAINT "pk_ticker" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "tweet" ADD CONSTRAINT "fk_tweet_user" FOREIGN KEY("user")
REFERENCES "user" ("id");

ALTER TABLE "tweet" ADD CONSTRAINT "fk_tweet_ticker" FOREIGN KEY("ticker")
REFERENCES "ticker" ("id");

