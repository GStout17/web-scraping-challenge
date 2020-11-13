# web-scraping-challenge

## Step 1 - Scraping
- Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
- Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of the scraping and analysis tasks. The following was completed
### Mars News & Facts
- Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. Assiged the text to variables for future refrence.
- Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.

### Mars Hemispheres
- Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
- Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
- Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application
- Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
- Converted the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape, which executed all of the scraping code from above and returned one Python dictionary containing all of the scraped data.
- Created a route called /scrape that will import your scrape_mars.py script and call your scrape function.
- Stored the teturn value in Mongo as a Python dictionary
- Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
- Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.



