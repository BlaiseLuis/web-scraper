
from ast import Try
import errno
import requests
from bs4 import BeautifulSoup
import html5lib
import csv
csv_file = open('scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'price', 'shipping'])

url = 'https://www.newegg.com/p/pl?d=video+cards'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

for contain in soup.find_all('div', class_='item-container'):
    title = contain.find_all('a', class_='item-title')
    title = (title[0].text)
    print(title)

    price = contain.find_all('li', class_='price-current')
    price = (price[0].text)
    print(price)

    try:
        shipping = contain.find_all('li', class_='price-ship')
        shipping = (shipping[0].text)
        if shipping == 'Free Shipping':
            print(shipping)

    except IndexError:
        print(None)

    print()

    csv_writer.writerow([title, price, shipping])
csv_file.close()


# container = soup.findAll('div', {'class': "item-container"})
# print(container.text)


# for article in soup.find_all("article"):
# headline = (article.h2.text)
# print(headline)
# summary = article.find('div', class_='entry-content').p.text
# print(summary)
# article = soup.find('article')
# vid_link = article.get( class_='youtube-player')['src']
# vid_id = vid_link.split('/')[4]
# vid_id = vid_id.split('?')[0]
# link = f'https://youtube.com/watch?v={vid_id}'

# print()


# for article in soup.find_all('td', class_="titlelink"):
#blog = article.a.text


#section = soup.find('div', class_='blog-content')
# for spoon in section:
#headline = spoon.h2
# print(headline)

# for spoon in soup.find_all('div', class_="blog-content"):
# headline = spoon.a.text
# print(headline)
