import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.example.com')
soup = BeautifulSoup(response.text, 'html.parser')

# Wyświetlenie tytułu strony
print("Title:", soup.title.string)

# Wypisanie wszystkich linków na stronie
for link in soup.find_all('a'):
    print(link.get('href'))
