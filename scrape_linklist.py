from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# Define the file path
file_path = "Link_List.txt"

# Open the file and read its contents
with open(file_path, 'r') as file:
    # Read all lines into a list and strip any leading/trailing whitespace
    links_array = [line.strip() for line in file.readlines()]

print(links_array[0])

def switch_tab(driver):
    x = driver.current_url
    if "getadblock" in x:
        driver.switch_to.window(driver.window_handles[0])
        print(x)

def click_cookie(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-1hv8ibq").click()
        time.sleep(2)
    except Exception as e:
        try: 
            driver.find_element(By.CSS_SELECTOR, "button.css-1hv8ibq").click()
        except Exception as e:
            print("No cookies")
            return

extension_path = "addblock.crx"
# options = webdriver.SafariOptions()
# options.add_extension(extension_path)
driver = webdriver.Safari()
driver.set_window_size(1000, 1000)

driver.get("first")

# Get total pages
time.sleep(5)
total_pages = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > div.MuiBox-root.mui-1y6f7x4 > div.MuiContainer-root.MuiContainer-maxWidthXl.mui-ho058c > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-9.SEARCHSTYLE-maxWidthContent.mui-1bnqu2k > div > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-sm-12.mui-2j7imh > div.MuiBox-root.mui-zzzt33 > nav > ul > li:nth-child(8) > a").text
print("Total Pages:", total_pages)

# Storage
array_data = []

# Array for looping through pages
page_count = ["x"] * int(total_pages)

# Array for looping through items
page_items = ["x"] * 10

# Check cookies
click_cookie(driver)
for count, item in enumerate(links_array):
    driver.get(links_array[count])
    print(f"Link #{count + 1}")

   
driver.quit()
