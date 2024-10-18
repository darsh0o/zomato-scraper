
**NOTE - only use for educational purposes 


# zomato-scraper
Zomato is basically not scrapable. After studying the underlying framework, you can basically divide it into two parts, one dealing with restaurant urls and the other with restaurant info. 


This project is a Zomato restaurant scraper built using **Python**, **Selenium**, and **BeautifulSoup**. It consists of two main scripts:
(for better results explore @botasaurus)

Scraping is only limited to publicly available data. Please do not scrape any privatised information. 

1. **`rest_urls.py`**: This script scrapes the URLs of all restaurants from a given Zomato page. Also specifiy the city inside the code for which you want to exract the data. 
2. **`rest_info.py`**: This script scrapes individual restaurant information such as name, description, phone number, aggregate rating, and more from the restaurant URLs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Running `rest_urls.py`](#running-rest_urlspy)
  - [Running `rest_info.py`](#running-rest_infopy)
- [Project Files](#project-files)
- [Explanation of Code](#explanation-of-code)
  - [Functions in `rest_urls.py`](#functions-in-rest_urlspy)
  - [Functions in `rest_infopy`](#functions-in-rest_infopy)
- [Requirements](#requirements)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/zomato-scraper.git
    cd zomato-scraper
    ```

2. **Install the dependencies**:

    Make sure you have Python installed. You can install all necessary packages using the `requirements.txt` file:
    
    ```bash
    pip install -r requirements.txt
    ```

3. **ChromeDriver Setup**:
    - This scraper uses **Selenium** to automate Chrome. You don't need to manually download the ChromeDriver, as the `webdriver-manager` will handle it automatically.

## Usage

### Running `rest_urls.py`

This script extracts restaurant URLs from a Zomato page.

1. Open `rest_urls.py`.
2. Replace the `page_url` variable with the Zomato URL of the page you want to scrape.
    ```python
    page_url = "https://www.zomato.com/mumbai/lower-parel-restaurants"
    ```
3. Run the script:
    ```bash
    python rest_urls.py
    ```
4. The script will scrape all restaurant URLs from the provided Zomato page and save them in a file named `restaurant_urls.txt`.

### Running `rest_info.py`

Once you have the restaurant URLs, use this script to extract detailed information about each restaurant.

1. Open `restaurant_urls.txt` and copy the URLs into the `restaurant_urls` list in `rest_info.py`.
2. Run the script:
    ```bash
    python rest_info.py
    ```
3. The scraped restaurant details will be displayed in the terminal and stored in a `restaurant_data.csv` file.

## Project Files

- **`rest_urls.py`**: Scrapes URLs of restaurants from a Zomato page.
- **`rest_info.py`**: Scrapes detailed restaurant information from each URL.
- **`restaurant_urls.txt`**: Contains the list of restaurant URLs (you can replace this with your own URLs).
- **`restaurant_data.csv`**: Output file containing scraped restaurant data.

## Explanation of Code

### Functions in `rest_urls.py`

- **`get_restaurant_urls(page_url)`**:
    - Initializes Selenium with ChromeDriver.
    - Loads the Zomato page and scrolls down to reveal more restaurants.
    - Extracts the URLs of the restaurants by parsing the page's JSON data and returns a list of URLs.

### Functions in `rest_info.py`

- **`get_restaurant_data(url)`**:
    - Opens the restaurant URL using Selenium.
    - Extracts the name, description, image, phone number, rating, review count, and cuisine type using BeautifulSoup.
    - Handles any page load or data extraction errors gracefully by using timeout mechanisms.

## Requirements

This project relies on the following Python packages:

- `selenium`: To automate Chrome for web scraping.
- `webdriver-manager`: To automatically manage ChromeDriver installations.
- `beautifulsoup4`: For parsing the restaurant's HTML content.
- `pandas`: For saving the scraped data into a CSV file.

The `requirements.txt` includes all the necessary dependencies:



