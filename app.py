# import dependecies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up Flask
app = Flask(__name__)

# use flask_pymongo to set up mongo comnnection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define HTML route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

# set up scraping route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"set":mars_data}, upsert=True)
    return redirect('/', code = 302)

.update_one(query_parameter, {"$set": data}, options)

if __name__ == "__main__":
    app.run()

# visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# optional delay for loading the page
browser.its_element_present_by_css('div.list_text', wait_time=1)

#convert the browser html to a soup objecgt and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

