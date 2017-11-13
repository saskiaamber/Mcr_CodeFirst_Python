from flask import Flask, render_template, request, redirect, session
from helpers.twitter import authenticate, collect_tweets

app = Flask("APIs query for CFG")
session = {}

@app.route('/')
def index():
    """ This will be the landing page for the app we will be using:
    this is intended to serve as an app accessing and displaying data from
    APIS"""
    return render_template('index.html', title = 'Landing page')

@app.route("/twitter")
def twitter_handler():
    """ This should display a form where the users introduce the terms
    they want to look for in Twitter"""
    return render_template("twitter.html")

@app.route("/twitter_search", methods = ['POST'])
def twitter_search_app():
    """When the search is submitted from the previous page,
    this function passes the form data to our python scripts
    and uses them to perform the query. It will then return the tweets
    and display them in /tweets_show"""
    query = request.form['query']
    tweets = collect_tweets(query)

    return render_template('tweets_show.html', search_string=query,
                           tweets =tweets)


@app.route("/spotify")
def spotify_handler():
    """ This should display a form where the users introduce the terms
    they want to look for in Twitter"""
    return render_template("spotify.html")


# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)