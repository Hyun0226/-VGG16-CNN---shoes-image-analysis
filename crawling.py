import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def PageUrl (pageNum):
    url = "https://abcmart.a-rt.com/display/category/main?genderGbnCode=10000&ctgrNo=1000000441&page=" + str(pageNum)
    return url

pageUrl = PageUrl(1)
driver.get(pageUrl)
    
cnt = 1
for i in range(13):
    pageUrl = PageUrl(1 + i)   
    driver.get(pageUrl)
    items = driver.find_elements(By.CSS_SELECTOR, ".search-prod-image")
    
    for item in items:
        try:
            time.sleep(0.5)          
            imgUrl = item.get_attribute("src")
            urllib.request.urlretrieve(imgUrl, str(cnt) + "s.jpg")
            cnt = cnt +1
            
        except Exception as e:
            print(e)
            pass

driver.close()


# //*[@id="searchList"]/li[9]/div[4]/div[1]/a/img





# for i in range(int(totalPageNum)):
#     pageUrl = PageUrl(FindingItemName, i+1)
#     driver.get(pageUrl)
#     time.sleep(2)
#     items = driver.find_elements(By.CSS_SELECTOR, ".lazyload.lazy")
#     print("Finding: ", FindingItemName, " - Page ", i+1, "/",totalPageNum, " start - ", len(items), " items exist")
#     for k in range(40):
#         try:
#             time.sleep(0.5)
#             images = driver.find_elements(By.CSS_SELECTOR, ".lazyload.lazy")[k].click()
#             time.sleep(2)
#             item = driver.find_element(By.XPATH, "//*[@id='bigimg']")
#             imgUrl = item.get_attribute("src")        
#             urllib.request.urlretrieve(imgUrl, str(cnt) + ".jpg")
#             cnt = cnt +1
#             driver.back()
#         except Exception as e:
#             print(e)
#             pass

# driver.close()
