from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


file_path = "Link_List.txt"
if os.path.exists(file_path):
    open(file_path, 'w').close()
else:
    with open(file_path, 'w') as file:
        pass

file_path_2 = "Link_Count.txt"
if os.path.exists(file_path_2):
    open(file_path_2, 'w').close()
else:
    with open(file_path_2, 'w') as file:
        pass

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
        print("No cookies")
        try: 
            driver.find_element(By.CSS_SELECTOR, "button.css-1hv8ibq").click()
        except Exception as e:
            return

extension_path = "addblock.crx"
# options = webdriver.SafariOptions()
# options.add_extension(extension_path)
driver = webdriver.Safari()
driver.set_window_size(1000, 1000)

driver.get("https://www.proff.dk/segmentering?phone=true&mainUnit=true&email=true&postalAddress=true&page=1")

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

for count, item in enumerate(page_count):
    driver.get(f"https://www.proff.dk/segmentering?phone=true&mainUnit=true&email=true&postalAddress=true&page={count + 1}")
    print(f"Page #{count + 1}")
    print()
    for countx, item in enumerate(page_items):
        x = count
        y = count+1
        z = countx
        p = countx+1
        mellemregning_1 = str(y)+str(0)
        mellemregning_2 = str(x)+str(p)
        if countx+1 == 10:
            resulat = int(mellemregning_1)
        else:
            resulat = int(mellemregning_2)
        print("Link #"+str(resulat))
        link = driver.find_element(By.CSS_SELECTOR, f"#__next > main > div > div.MuiBox-root.mui-1y6f7x4 > div.MuiContainer-root.MuiContainer-maxWidthXl.mui-ho058c > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-9.SEARCHSTYLE-maxWidthContent.mui-1bnqu2k > div > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-sm-12.mui-2j7imh > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.mui-tj3eis > div:nth-child({countx + 1}) > div > div > h2 > a").get_attribute("href")
        print(link)
        array_data.append(link)
        if countx+1 == 10:
            break
        if resulat == 10*count+1:
            with open(file_path, 'a') as file:
                for link in array_data:
                    file.write(link + '\n')

            with open(file_path_2, 'a') as file:
                if array_data: 
                    file.write(array_data[-1] + '\n')
    else:
        pass
driver.quit()
