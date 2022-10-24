from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flax_pymongo to setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
  
# Setup App Routes
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    # print("Mars: " + mars)
    return render_template("index.html", mars=mars)
    
# Setup Scraping Route",
# The button of the web app.",
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all() 
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)
    
# tell Flask to run
if __name__ == "__main__":
    app.run()