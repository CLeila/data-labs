# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1  2019

@author: leila
"""

class MySpider:
    """This class is created to scrape some easy website.
    It can check whetever the request has a good response and provide a soup 
    """
    def __init__(self, url_pattern, pages_to_scrape=10, sleep_interval=-1, scraper=None):
        self.url_pattern=url_pattern
        self.pages_to_scrape=pages_to_scrape
        self.sleep_interval=sleep_interval
        self.scraper= scraper
    
    def get_response_content(self, r):
        if (r.status_code == 200):
            return r.content
        else:
            print(r.status_code)
            return False
        
    def scrape_url(self,url):
        import requests as rq
        try:
            header= {
    'path': '/fr/all-games?prefn1=productTypeRefinementString&sz=16&format=page-element&prefv1=games&start=64',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'cookie':'__cfduid=d75502d5e38ba7e66b95cde9bebc867b81572625411; cqcid=abIbx608U7aQE9fZarr9kvKVbr; prefCountry=fr; dwanonymous_e2d89c436a26bc47381bc6c2fe1f51cc=abIbx608U7aQE9fZarr9kvKVbr; __cq_dnt=0; dw_dnt=0; dwac_decTgiaaiu1Xoaaadq5HbGM599=62Blf52ClEM0pLZE81sOukit2XabUTcFWoI%3D|dw-only|||EUR|false|Europe%2FParis|true; sid=62Blf52ClEM0pLZE81sOukit2XabUTcFWoI; dwsecuretoken_e2d89c436a26bc47381bc6c2fe1f51cc=JO6-fyUt8EvnjoUx_fk-XQRmqVNSIuC7cg==; dwsid=P0FB02CVzX2vb2tYgMrqxZyM_dpmRm47wUnaxZEFJ3E7iyV-I8y1s2ycqisCqFm2sAE87IixV5a3kd3CwTFXJA==',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    } 
            response = rq.get(url,headers=header,timeout= 20)
            content=self.get_response_content(response)
            if not (self.scraper is None):
                result = self.scraper(content)
            else:
                result=content
        except:
            result=None
        print(result)
        return result

def soup_pretty(html):
    from bs4 import BeautifulSoup
    import pandas as pd
    soup=BeautifulSoup(html)
# selected elements and cleaning of each one by one
    title =[element.text for element in soup.select('h2.prod-title')]
    rows_t = [row.strip().replace('\n\n','\n') for row in title]
    date =[element.text for element in soup.select('.release-date.only-on-list')]
    rows_d = [row.strip().replace('\n\n','\n').split('\n')[1] for row in date]
    p_original = [element.text for element in soup.select('span.price-item')]
    rows_original = [row.strip().replace(' €','').replace(',','.') for row in p_original]
    floats = [float(x) for x in rows_original]
    p_promo = [element.text for element in soup.select('span.price-sales')]
    rows_promo = [row.strip().replace(' €','').replace(',','.') for row in p_promo]
    floats_promo = [float(x) for x in rows_promo]
    edition= [element.text for element in soup.select('.card-subtitle h3')]
    rows_ed = [row.strip().replace(' Edition','').replace('Édition ','') for row in edition]
# DF of all my elements 
    df = pd.DataFrame()
    df['parution_date']=[i for i in rows_d]
    df['title']=[i for i in rows_t]
    df['edition']=[i for i in rows_ed]
    df['promotion_price']=[i for i in floats_promo]
    df['original_price']=[i for i in floats]
    df['%']=round((1-(df['promotion_price']/df['original_price']))*100,2)
   # df = df.append(df)
    return (df)
 
sp = MySpider('https://store.ubi.com/fr/all-games?prefn1=productTypeRefinementString&sz=16&format=page-element&prefv1=games&start=64', scraper=soup_pretty)


