import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(response.text[:400])