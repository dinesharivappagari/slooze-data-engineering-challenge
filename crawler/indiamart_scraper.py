from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# Path to your actual ChromeDriver
CHROME_DRIVER_PATH = "C:\\Users\\DINESH\\slooze_data_engineering_challenge\\chromedriver.exe"

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Create output directory if not exists
os.makedirs("../data", exist_ok=True)

def scrape_indiamart(pages=3):
    base_url = "https://dir.indiamart.com/impcat/industrial-machinery.html"
    results = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        driver.get(f"{base_url}?page={page}")

        # Wait until product listings appear
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"lstng-card")]'))
            )
        except:
            print("Timeout — listings not found.")
            continue

        listings = driver.find_elements(By.XPATH, '//div[contains(@class,"lstng-card")]')

        for item in listings:
            try:
                title = item.find_element(By.XPATH, './/h2').text.strip()
            except:
                title = None
            try:
                price = item.find_element(By.XPATH, './/span[contains(text(),"₹")]').text.strip()
            except:
                price = None
            try:
                location = item.find_element(By.XPATH, './/span[contains(@class,"cmpny-loc")]').text.strip()
            except:
                location = None

            results.append({
                "Product Name": title,
                "Price": price,
                "Location": location
            })

    driver.quit()

    df = pd.DataFrame(results)
    df.to_csv("../data/industrial_machinery.csv", index=False)
    print("✅ Scraping complete. Data saved.")
