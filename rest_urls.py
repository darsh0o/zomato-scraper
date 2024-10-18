# scrape_restaurant_urls.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time

def get_restaurant_urls(page_url):
    # Initialize WebDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Set a reasonable timeout for loading the page
    driver.set_page_load_timeout(30)
    
    try:
        driver.get(page_url)
    except TimeoutException:
        print(f"Page load timed out for {page_url}.")
        driver.quit()
        return []
    
    # Use a more general approach to wait for recognizable content
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Waiting for the body tag as a general indicator
        )
    except TimeoutException:
        print(f"Elements took too long to load for {page_url}.")
        driver.quit()
        return []
    
    # Scroll down the page for about a minute to load all restaurants
    scroll_pause_time = 5  # Adjust as needed
    total_scroll_time = 120  # Total scroll time in seconds
    end_time = time.time() + total_scroll_time

    while time.time() < end_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

    # Get the fully rendered page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find the script containing the JSON data
    script_tag = soup.find('script', string=lambda t: t and '"ItemList"' in t)
    if not script_tag:
        print(f"No JSON data found in {page_url}.")
        driver.quit()
        return []
    
    # Parse the JSON data
    try:
        json_data = json.loads(script_tag.string)
        base_url = "https://www.zomato.com"
        restaurant_urls = [f"{base_url}{item['url']}" for item in json_data['itemListElement']]
    except (json.JSONDecodeError, KeyError):
        print(f"Error parsing JSON data in {page_url}.")
        restaurant_urls = []
    
    driver.quit()
    return restaurant_urls

if __name__ == "__main__":
    # URL of the Zomato page containing the list of restaurants
    page_url = "https://www.zomato.com/mumbai/lower-parel-restaurants"  # Replace with the actual page URL
    
    restaurant_urls = get_restaurant_urls(page_url)
    
    if restaurant_urls:
        print(f"Found {len(restaurant_urls)} restaurant URLs:")
        for url in restaurant_urls:
            print(url)
    else:
        print("No restaurant URLs found.")
    
    # Save the URLs to a file for further use
    with open("restaurant_urls_mumbai.txt", "w") as file:
        for url in restaurant_urls:
            file.write(url + "\n")

