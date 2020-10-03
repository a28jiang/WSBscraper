import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
import time

# VARIABLES
DRIVER_PATH = '/Users/aaronjiang/chromedriver'
targetPage = 'https://www.reddit.com/r/wallstreetbets/comments/igw84c/daily_discussion_thread_for_august_26_2020/?sort=confidence'
setDelay = 1

# CLASS SELECTORS
allClass = '_3tw__eCCe7j-epNCKGXUKk'

userClass = 'f3THgbzMYccGW8vbqZBUH'
delUserClass = '_1S45SPAIb30fsXtEcKPSdt'

pointClass = '_3_GZIIN1xcMEC5AVuv4kfa'

commentClass = '_1qeIAgB0cPwnLhDF9XSiJM'
deletedComment = '_2Wu4MNMVl4bsJ9iVnQz0dF'
richCommentClass = 'RichTextJSON-root'

moreComments = '_3_mqV5-KnILOxl1TvgYtCk'
firstComments = '._2JBsHFobuapzGwpHQjrDlD'


options = Options()
options.headless = True
options.add_argument("--incognito")


driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(targetPage)


loadFirst = driver.find_element_by_css_selector(firstComments)
loadFirst.click()
time.sleep(5)

timedOut = False
iteration = 0

while not timedOut:
    try:
        loadMore = driver.find_element_by_class_name(moreComments)
        print("Sraping...")
        loadMore.click()
        iteration += 1

        time.sleep(setDelay)

    except:
        timedOut = True
        print("Comments timed out at " + str(iteration))


comments = driver.find_elements_by_class_name(allClass)

with open('comments.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for comment in comments:

        # DELETED COMMENT
        try:
            isDeleted = comment.find_element_by_class_name(deletedComment).text
            print('DELETED COMMENT')

        except:

            try:
                # REGULAR COMMENT
                writer.writerow([comment.find_element_by_class_name(userClass).text, comment.find_element_by_class_name(
                    pointClass).text, comment.find_element_by_class_name(commentClass).text])
            except:

                # RICH TEXT COMMENT
                try:
                    writer.writerow([comment.find_element_by_class_name(userClass).text, comment.find_element_by_class_name(
                        pointClass).text, comment.find_element_by_class_name(richCommentClass).text])
                    print('RICH COMMENT FOUND')

                except:
                    print("COULD NOT HANDLE")


print("FINISHED")

driver.quit()
