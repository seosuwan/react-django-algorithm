import pandas as pd
from sklearn import preprocessing
from admin.common.models import ValueObject, Printer, Reader
from icecream import ic
import numpy as np
import datetime as dt
import csv
from selenium import webdriver
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from datetime import datetime
import re
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.pyplot


class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        #nltk.download()
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        # self.naver_movie()
        # self.tweet()
        self.samsung_report(vo)


    def samsung_report(self, vo):
        okt = Okt()
        daddy_bag = okt.pos('아버지 가방에 들어가신다', norm=True, stem=True)
        print(f':::::::: {datetime.now()} ::::::::\n {daddy_bag}')
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = f'{vo.context}kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            full_texts = f.read()
        line_removed_texts = full_texts.replace('\n', ' ')
        # print(f':::::::: {datetime.now()} ::::::::\n {line_removed_texts}')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        tokenized_texts = tokenizer.sub('', line_removed_texts)
        tokens = word_tokenize(tokenized_texts)
        # print(f':::::::: {datetime.now()} ::::::::\n {tokens}')
        noun_tokens = []
        for token in tokens:
            token_pos = okt.pos(token)
            noun_token = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(noun_token)) > 1:
                noun_tokens.append("".join(noun_token))
        # print(f':::::::: {datetime.now()} ::::::::\n {noun_tokens[:10]}')
        noun_tokens_join = " ".join(noun_tokens)
        tokens = word_tokenize(noun_tokens_join)
        # print(f':::::::: {datetime.now()} ::::::::\n {tokens}')
        stopfile = f'{vo.context}stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        stopwords.extend(['용량','각주','가능보고서','고려','전세계','릴루미노','가치창'])
        texts_without_stopwords = [text for text in tokens if text not in stopwords]
        # print(f':::::::: {datetime.now()} ::::::::\n {texts_without_stopwords[:10]}')
        freq_texts = pd.Series(dict(FreqDist(texts_without_stopwords))).sort_values(ascending=False)
        # print(f':::::::: {datetime.now()} ::::::::\n {freq_texts[:30]}')
        wcloud = WordCloud(f'{vo.context}D2Coding.ttf', relative_scaling=0.2,
                           background_color='white').generate(' '.join(texts_without_stopwords))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(f'{vo.context}wcloud.png')

    def naver_movie(self):

        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        vo.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        arr = [div.a.string for div in all_div]
        for i in arr:
            print(i)
        dt = {i + 1: val for i, val in enumerate(arr)}
        with open(vo.context + 'with_save.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(dt.keys())
            w.writerow(dt.values())

    def tweet(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome('admin/crawling/data/chromedriver', options=options)

        start_date = dt.date(year=2018, month=12, day=1)
        until_date = dt.date(year=2018, month=12, day=2)  # 시작날짜 +1
        end_date = dt.date(year=2018, month=12, day=2)
        query = 'obama'
        total_tweets = []
        url = f'https://twitter.com/search?q={query}%20' \
              f'since%3A{str(start_date)}%20until%3A{str(until_date)}&amp;amp;amp;amp;amp;amp;lang=eg'
        while not end_date == start_date:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                daily_freq = {'Date': start_date}
                word_freq = 0
                tweets = soup.find_all('p', {'class': 'TweetWextSize'})
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height != last_height:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    tweets = soup.find_all('p', {'class', 'TweetTextSize'})
                    word_freq = len(tweets)
                else:
                    daily_freq['Frequency'] = word_freq
                    word_freq = 0
                    start_date = until_date
                    until_date = dt.timedelta(days=1)
                    daily_freq = {}
                    total_tweets.append(tweets)
                    break
                last_height = new_height
        query_df = pd.DataFrame(columns=['id', 'message'])
        number = 1
        for i in range(len(total_tweets)):
            for j in range(len(total_tweets[i])):
                query_df = query_df.append({'id': number, 'message': (total_tweets[i][j]).text},
                                           ignore_index=True)
                number = number + 1
        print(query_df.head())