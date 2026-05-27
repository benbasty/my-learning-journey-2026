# if javascript is involved, to interact with websites use selenium
# every devices, browsers have their own user-agent string, 
# which identifies the web browser and is included in all HTTP requests.
# using requests, u r probably will be seen as a robot
# using selenium, u r probably to be pass a human
# cuz selenium user-agent is a same as the browser, got same traffic patterns
# However, websites can still find ways to detect Selenium, and major ticketing 
# and e-commerce websites often block it to prevent the web scraping of their pages.

from selenium import webdriver
browser = webdriver.Chrome()
print(type(browser))
browser.get('https://inventwithpython.com')
input("Press Enter to close the browser...")  # Keeps script alive
browser.quit()
