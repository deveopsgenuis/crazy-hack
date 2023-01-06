import os
from selenium import webdriver
from flask import Flask

app = Flask(__name__)

# Set the path to the Chromium executable
chromium_path = '/path/to/chromium'

@app.route('/')
def test():
  # Start the webdriver
  driver = webdriver.Chrome(executable_path=chromium_path)

  # Load the URL
  driver.get('https://ma-studio-deve.web.app/')

  # Find all the img tags on the page
  img_tags = driver.find_elements_by_tag_name('img')

  # Replace the src URLs with example.com
  for img in img_tags:
    img.set_attribute('src', 'http://www.example.com')

  # Close the webdriver
  driver.quit()

  # Return the modified page HTML as a response
  return driver.page_source

if __name__ == '__main__':
  app.run(port=4000)