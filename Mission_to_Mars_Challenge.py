#!/usr/bin/env python
# coding: utf-8

# In[116]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[117]:


# Path to chromedriver
get_ipython().system('where chromedriver')


# In[118]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': r'C:\Users\Assaci\Class\Mission-to-Mars\chromedriver.exe'}
browser = Browser('chrome', **executable_path)


# ### Visit the NASA Mars News Site

# In[119]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[120]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[121]:


slide_elem.find("div", class_='content_title')


# In[122]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[123]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[124]:


# Visit URL
#url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#browser.visit(url)


# In[125]:


# Find and click the full image button
#full_image_elem = browser.find_by_id('full_image')
#full_image_elem.click()


# In[126]:


# Find the more info button and click that
#browser.is_element_present_by_text('more info', wait_time=1)
#more_info_elem = browser.links.find_by_partial_text('more info')
#more_info_elem.click()


# In[127]:


# Parse the resulting html with soup
#html = browser.html
#img_soup = soup(html, 'html.parser')


# In[128]:


# find the relative image url
#img_url_rel = img_soup.select_one('figure.lede a img').get("src")
#img_url_rel


# In[129]:


# Use the base url to create an absolute url
#img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
#img_url


# ### Mars Facts

# In[130]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[131]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[132]:


df.to_html()


# ### Mars Weather

# In[133]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[134]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[135]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[136]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[137]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

links = browser.find_by_css('a.product-item h3')

# Loop through the links 
for i in range(len(links)):
    hemisphere = {}
    
    # find elements on each loop and click on link
    browser.find_by_css('a.product-item h3')[i].click()
    
    # find Sample image anchor tag and extract the href
    samp_element = browser.find_link_by_text('Sample').first
    img_url = samp_element['href']
    hemisphere["img_url"] = img_url
    
    # Get hemisphere title
    title = browser.find_by_css("h2.title").text
    hemisphere["title"] = title
    
    # Append hemisphere object to list hemisphere_image_urls
    hemisphere_image_urls.append(hemisphere)
    # Navigate back
    browser.back()


# In[138]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[140]:


# 5. Quit the browser
browser.quit()


# In[ ]:




