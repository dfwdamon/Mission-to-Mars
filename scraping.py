#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page. 
# The is_element_present_by_css looks for element combo of tag, div & attribute list_text. 
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Setup HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
# ?? How is this the parent element?
slide_elem = news_soup.select_one('div.list_text')
# slide_elem = news_soup.select_one('div.card')

# this chains .find onto the previous variable slide_elem. variable holds a lot of info.
# and look inside of that info to find specific data.
slide_elem.find('div', class_='content_title')
# slide_elem.find('div', class_='card')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title')
# news_title = slide_elem.find('p', class_='card-text').get_text()
news_title

# Use the parent element to find the paragraph text.
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup, so we can scrape the full-size image URL.
html = browser.html
img_soup = soup(html, 'html.parser')

# Now find relative image url. .get('src')pulls the link to the image.
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL.
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()
browser.quit()


