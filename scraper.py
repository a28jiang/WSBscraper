from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
import time
DRIVER_PATH = '/Users/aaronjiang/chromedriver'


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.reddit.com/r/wallstreetbets/comments/igw84c/daily_discussion_thread_for_august_26_2020/?sort=confidence")

# https://www.reddit.com/r/wallstreetbets/search?q=discussion%20thread&restrict_sr=1&sort=new
# initial loadAll button
loadAll = driver.find_element_by_css_selector("._2JBsHFobuapzGwpHQjrDlD")
loadAll.click()
time.sleep(10)

comments = driver.find_elements_by_class_name('_3tw__eCCe7j-epNCKGXUKk')


for comment in comments:
    print(comment.text+'\n')


# for i in range(0, amount):
#     try:
#         loadMoreButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#             driver.find_element_by_id('moreComments')))
#         print(loadMoreButton.text)
#         loadMoreButton.click()
#         time.sleep(2)
#     except Exception as e:
#         print(e)
#         break


# try:
#     loadAll = driver.findElement(By.class("_2JBsHFobuapzGwpHQjrDlD"))
#     print('Successfully loaded more')
# except NoSuchElementException:
#     print('Load button not found')


# print(loadAll)
# clickLoadAll = driver.find_element_by_class_name(
#     '_2JBsHFobuapzGwpHQjrDlD j9NixHqtN2j8SKHcdJ0om _2nelDm85zKKmuD94NequP0').click()


# getMore = driver.find_element_by_class_name(
#     '_2HYsucNpMdUpYlGBMviq8M _23013peWUhznY89KuYPZKv')
# print(geMore)


# print(driver.page_source)
driver.quit()
