import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        # Add more user-agents as needed
    ]
    return random.choice(user_agents)


def perform_web_scraping(url):
    # Configure Chrome options
    options = Options()
    options.headless = True

    # Set user-agent
    options.add_argument(f"user-agent={get_random_user_agent()}")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load (adjust the timeout as needed)
        wait = WebDriverWait(driver, 10)
        # Simulate human-like behavior
        time.sleep(random.uniform(1, 3))

        # Scraping logic here
        if url == "https://stockx.com/sneakers":

            product_tiles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="productTile"]')))

            for product_tile in product_tiles:
                # Extract inner information from the product tile
                product_link = product_tile.find_element(
                    By.CSS_SELECTOR, 'a[data-testid="productTile-ProductSwitcherLink"]').get_attribute('href')
                product_name = product_tile.find_element(By.CSS_SELECTOR, 'p.css-3lpefb').text
                lowest_ask = product_tile.find_element(By.CSS_SELECTOR, 'p.css-nsvdd9').text

                # Print or save the extracted information
                print(f"Product Link: {product_link}")
                print(f"Product Name: {product_name}")
                print(f"Lowest Ask: {lowest_ask}")
                print("\n")

        elif url == "https://www.klekt.com/sneakers":

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[itemprop="offers"]')))
            product_pods = driver.find_elements(By.CSS_SELECTOR,'div.c-product-pod.u-flex.u-flex--col.u-flex--justify-between.u-padding\\@country.pod-botton-tiny-padding.u-padding-small[itemprop="offers"]')

            for product_pod in product_pods:
                # Extract details based on the structure
                product_link = product_pod.find_element(By.CSS_SELECTOR, 'a.pod-link').get_attribute('href')
                product_name = product_pod.find_element(By.CSS_SELECTOR, 'h3.pod-name').text
                product_price = product_pod.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').text

                # Print or process the extracted details
                print(f"Product Link: {product_link}")
                print(f"Product Name: {product_name}")
                print(f"Product Price: {product_price}")
                print("\n")

    finally:
        # Close the WebDriver
        driver.quit()

# Example usage
urls_to_scrape = ["https://www.klekt.com/sneakers", "https://stockx.com/sneakers"]
for url in urls_to_scrape:
    perform_web_scraping(url)
