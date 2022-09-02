import requests
import string
import os

from bs4 import BeautifulSoup

# link = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'

number_of_pages = int(input())
type_of_articles = input()
for j in range(number_of_pages):
    os.makedirs('Page_{}'.format(j+1))
    r = requests.get('https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=' + str(j+1))
    if r.status_code // 100 != 2:
        print('The URL returned {}'.format(r.status_code))
        exit()

    soup = BeautifulSoup(r.content, 'html.parser')
    cont = soup.prettify(encoding='UTF-8')
    articles = soup.find_all('article')
    articles_num = []
    articles_name = []
    links = []

    for i in range(len(articles)):
        if articles[i].find('span', {'class': 'c-meta__type'}).text == type_of_articles:
            articles_num.append(i)

    for i in articles_num:
        a = articles[i].find('a')
        href = a.get('href')
        a = articles[i].find('a').text
        new_a = ''.join(i for i in a if i not in string.punctuation)
        new_a = new_a.replace(" ", '_')
        articles_name.append(new_a)
        links.append(href)

    for i in range(len(links)):
        file = open('Page_{}/{}.txt'.format(j+1, articles_name[i]), 'wb')
        q = requests.get('https://www.nature.com'+links[i])
        soup_1 = BeautifulSoup(q.content, 'html.parser')
        texts = soup_1.find('div', {'class': 'c-article-body u-clearfix'}).text
        file.write(texts.encode())
        file.close()

print('Saved all articles')

