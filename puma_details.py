from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Creates Chrome WebDriver instance.
driver = webdriver.Chrome()

# Let's maximize the automated chrome window
driver.maximize_window()

# Navigate to Puma website
driver.get("https://in.puma.com/in/en/search?q=shoes&pref_gender=Unisex%2CMale%2CFemale")

# Wait for the page to load
time.sleep(3)

# Close the pop-up dialog (if it appears)
try:
    x = driver.find_element(By.XPATH, '//*[@id="puma-skip-here"]/section/div[2]/button[1]')
    x.click()
except:
    pass
time.sleep(2)

# Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
time.sleep(2)
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(3)
    if new_height == last_height:
        break
    last_height = new_height

# # Use a try-except block to handle TimeoutException
# try:
#     # Wait for the products to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-test-id="product-list-item"]')))
# except selenium.common.exceptions.TimeoutException:
#     print("TimeoutException: Product list not found within the specified time. Proceeding with the code.")

# Imports the HTML of the webpage into python
soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.set_script_timeout(10)
# grabs the HTML of each product
product_card = soup.find_all('li', {'data-test-id': 'product-list-item'})

data = []

# Grabs the product details for every product on the page and adds each product as a row in our dataframe
for product in product_card:
    try:
        link = product.find('a', class_='tw-hqslau').get('href')
        data.append({"Link": link })
    except:
        pass

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv("Puma_links_data_part_1.csv", index=False)

# Close the Chrome WebDriver
driver.quit()