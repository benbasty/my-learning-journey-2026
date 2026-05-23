# web scraping is a term for using a program to download and process content from the web.

# modules that make it easy to scrape web pages on the web

    # webbrowser Comes with Python and opens a browser to a specific page

    # requests Downloads files and web pages from the internet

    # Beautiful Soup (bs4) Parses HTML to extract the information you want

    # Selenium Launches and controls a web browser, such as by filling in forms and simulating mouse clicks

    # Playwright Launches and controls a web browser; newer than Selenium and has some additional features

#These will be used for learning purposes only. I will probably be using more 
# advanced technologies and AI models based scrapping methods such as 
# httpx (async) + parsel (XPath/CSS selectors, faster than BeautifulSoup)
# Playwright (instead of Selenium)
# curl_cffi for TLS fingerprinting
# Scrapy + Scrapy Playwright for large‑scale projects
# Residential proxy integration (e.g., with scrapy-rotating-proxies)

# 1 webbrowser: opens a browser to a specific page

import webbrowser
webbrowser.open('https://inventwithpython.com/')
