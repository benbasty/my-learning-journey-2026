import requests
import sys
import webbrowser
import bs4

print('Searching...')  # Display text while downloading

# Download the search results page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()  # Stop if download failed

# Parse the HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find all result links (current PyPI class is 'package-snippet')
link_elems = soup.select('.package-snippet')

# Number of tabs to open (max 5, or fewer if less results)
num_open = min(5, len(link_elems))

for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)