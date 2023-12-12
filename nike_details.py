from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

url = "https://www.nike.com/in/t/air-force-1-07-shoes-WrLlWX/CW2288-111"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
buy_tools_div = driver.find_element(By.ID, 'buyTools')
size_parent_div = buy_tools_div.find_element(By.CLASS_NAME,'css-12whm6j')
all_sizes = driver.find_elements(By.NAME, 'skuAndSize')
size_count = 0
for size in all_sizes:
    # input_tag = size.find_element(By.TAG_NAME, 'input')
    disabled_value = size.get_attribute('disabled')
    if disabled_value is None:
        size_count = size_count + 1
print(size_count)
all_colors = driver.find_elements(By.CLASS_NAME, 'css-7aigzk')
for color in all_colors:
    image_tag = size.find_element(By.TAG_NAME, 'img')
    color_name = image_tag.get_attribute('alt')
    
    if disabled_value is None:
        size_count = size_count + 1
# all_children_by_css = size_parent_div.find_element(By.CLASS_NAME, '*')