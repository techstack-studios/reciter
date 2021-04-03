import requests
import re
import numpy as np

from collections import defaultdict

poems = defaultdict(list)


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    response = requests.get(url, headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(
        r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(
        r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents_tags = re.findall(
        r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in contents_tags:
        content = re.sub(r'<.*?>', '', content)
        contents.append(content.strip())

    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems[title].append(poem)
    #for poem  in poems:
        #print(poem[0]['contents'])
        #print('---'*80)


def main():
    url = 'https://www.gushiwen.org/shiwen/default_0AA1.aspx'
    for page in range(1, 20):
        url = url = 'https://www.gushiwen.org/shiwen/default_0AA%s.aspx' % page
        print("reading page ", page)
        parse_page(url)

    np.save('poems.npy', poems)


if __name__ == '__main__':
    main()