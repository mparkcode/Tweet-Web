import os
from flask import Flask, render_template,redirect,request
from search_tweets import search

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/results")
def results():
    q = request.args.get("q")
    tweets = search(q,10)
    return render_template("results.html", tweets=tweets)
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)



