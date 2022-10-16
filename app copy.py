{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1a4040a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10.5.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6e11bfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.\n",
    "# The second line says we'll use PyMongo to interact with our Mongo database.\n",
    "# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.\n",
    "\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fada8343",
   "metadata": {},
   "outputs": [],
   "source": [
    "# setup Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0ff2be4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flax_pymongo to setup mongo connection.\n",
    "# app.config tells Python that our app will connect to Mongo using a URI. \n",
    "# \"mongodb:...\" is the URI to cnnect app to Mongo. and the db named mars_app.\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58ac4bcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup App Routes\n",
    "# Setup Flaks routes: one for the main HTML page for viewers, one to scrape new data using the written code.\n",
    "# Tells Flask what to display when looking @ the home page.\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "# uses pymongo to find the mars collection in our db.\n",
    "    mars = mongo.db.mars.find_one()\n",
    "# tells Flask to return an HTML template using an index.html file.  mars=mars tells Python to use the mars collection in mongodb.   \n",
    "    return render_template(\"index.html\", mars=mars)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b0113cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup Scraping Route\n",
    "# The button of the web app.\n",
    "# Defines the route Flask will use.\n",
    "@app.route(\"/scrape\")\n",
    "def scrape()\n",
    "# assign a new variable that points to Mongo db.\n",
    "    mars = mongo.db.mars\n",
    "# create new variable to hold the newly scraped data. reference the scrape_all func. in the scraping.py file exported from Jupyter.\n",
    "    mars_data = scraping.scrape_all()\n",
    "# update the db using .update_one.\n",
    "    mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "#     adds redirect after scraping data. navigate our page back to / where we can see updated content.\n",
    "    return redirect('/', code=302)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d83c73c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# tell Flask to run\n",
    "if __name__ == \"__main__\"\n",
    "    app.run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b121be73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
