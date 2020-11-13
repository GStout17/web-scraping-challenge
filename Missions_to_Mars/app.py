# Importing
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo for  connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route for index
@app.route("/")
def home():

    # Find one record of data from the mongo database (find_one)
    mars_info = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function from the scrape python file
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)