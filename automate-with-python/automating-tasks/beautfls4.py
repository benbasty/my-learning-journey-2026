import requests, bs4
# download the main page
res = requests.get('https://autbor.com/example3.html')
# verify that an HTTP request was successful
# res.raise_for_status()
# uses Beautiful_Soup to parse the response text into HTML format
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(example_soup)