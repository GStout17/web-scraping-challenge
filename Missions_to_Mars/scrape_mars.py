
# importing
import pandas as pd
import pymongo
import requests

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs

# New window
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Scrap Mars News
def mars_news(browser):

    # connection to site
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    # BS
    html = browser.html
    soup = bs(html,'html.parser')

    try:
        # Title/summary
        slide = soup.select_one("ul.item_list li.slide")
        title = slide.find('div',class_='content_title').text
        paragraph = slide.find('div',class_='article_teaser_body').text
    except:
        return None, None
        
    # title & paragraph text
    return title, paragraph

# scapre image from mars
def mars_featureImg(browser):
    # set connection to the news site
    mars_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_image_url)

    # find the button to click
    full_image_button = browser.find_by_id('full_image')

    # clicks the button and brings us to the full image
    full_image_button.click()

    # splinter for more info
    moreInfo_button = browser.links.find_by_partial_text('more info')
    moreInfo_button.click()

    # activate the ability to parse the webpage
    html = browser.html
    img_soup = bs(html,'html.parser')

    # image location
    img_url = img_soup.find('figure',class_='lede').find('a').get('href')
    img_url = 'https://www.jpl.nasa.gov'+img_url

    # Return image url
    return img_url

# Scrap mars facts
def mars_facts(browser):
    # Connection to site
    marsFacts_url = 'https://space-facts.com/mars/'
    browser.visit(marsFacts_url)
    
    # Grabbing info
    facts_table = pd.read_html(marsFacts_url)

    # Index 0
    mars_df = facts_table[0]

    # Rename columns
    mars_df.columns = ['Fact','Value']

    # Returing mars facts table
    return mars_df

# Scrap hemisphere data
def hemisphere_images(browser):
    # Setting connection to site
    mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hem_url)

    # Parsing
    html = browser.html
    hem_soup = bs(html,'html.parser')

    # Item/containers
    hem_url = hem_soup.find_all('div',class_='item')

    # Creating dic/loop
    hem_dict = []
    for hem in range(len(hem_url)):
        hem_item = {}    
        # click on each of the links
        browser.find_by_css('a.product-item h3')[hem].click()
        # get the enhanced image title
        hem_item["img_title"] = browser.find_by_css('h2.title').text
        # get the enhanced image link
        hem_item["img_url"] = browser.links.find_by_text('Sample')['href']
        # add it to the hemisphere dictionary
        hem_dict.append(hem_item)
        # have to go back to the main browser page
        browser.back()

    # return the hemisphere image info
    return hem_dict

# Grabing infomation from scraping functions
def scrape():
    # call the functions
    title, paragraph = mars_news(browser)
    featureImg_url = mars_featureImg(browser)
    table = mars_facts(browser)
    hem_img = hemisphere_images(browser)

    # Dictionary for storing
    data = {
        "news_title":title,
        "news_paragraph":paragraph,
        "featured_image_url":featureImg_url,
        "facts":table,
        "hemisphere_images":hem_img
    }
    
    # quit 
    browser.quit()
    return data

print(scrape())

