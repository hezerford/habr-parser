from bs4 import BeautifulSoup
import random
import json
import requests
import datetime

headers = {
    'accept': 'application/json, text/plain, */*',
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36'
}

article_dict = {}

for i in range(1, 4):
    url = f'https://habr.com/ru/top/daily/page{i}/'

    req = requests.get(url, headers=headers).text
    
    #собираем html код страницы в файл

    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(src)

    soup = BeautifulSoup(req, 'lxml')
    all_hrefs_articles = soup.find_all('a', class_='tm-article-snippet__title-link') # получаем статьи

    for article in all_hrefs_articles: # проходимся по статьям
        article_name = article.find('span').text # собираем названия статей
        article_link = f'https://habr.com{article.get("href")}' # ссылки на статьи
        article_dict[article_name] = article_link

    # with open("articles.json", "w", encoding='utf-8') as f: 
    #     json.dump(article_dict, f, indent=4, ensure_ascii=False).replace("},", "},\n")

with open(f"articles_{datetime.datetime.now().strftime('%d_%m_%Y')}.json", "a", encoding='utf-8') as f: 
    try:
        json.dump(article_dict, f, indent=4, ensure_ascii=False)
        print('Статьи были успешно получены')
    except:
        print('Статьи не удалось получить')