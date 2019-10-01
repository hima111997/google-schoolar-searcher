# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:02:36 2019

@author: mohamed
"""
import requests, webbrowser,urllib, time
from bs4 import BeautifulSoup

url = []
page = 10



def main(url,page):
    
    user_input= input('please enter the google schooler URL: ')
    r = requests.get(user_input).text
    soup = BeautifulSoup(r,'html.parser')
    
    
    '''openening the first 10 files in a google schoolar Url'''
    def opener(com_url_pages,soup):
        
        '''openning the first page'''
        for i in soup.find_all(id ='gs_res_ccl_mid'):
            for p in i.find_all('a'):
                if p.get('href').startswith('http'):
                    #print(p.get('href'))
                    if p.get('href').endswith('.pdf'):
                        print ('there are some pdf files ', p.get('href'))
                    else: 
                        time.sleep(10)
                        webbrowser.open(p.get('href'))
        
        '''openning the rest of pages'''
        for i in com_url_pages:
            r = requests.get(i).text
            soup = BeautifulSoup(r,'html.parser')
            for i in soup.find_all(id ='gs_res_ccl_mid'):
                for p in i.find_all('a'):
                    if p.get('href').startswith('http'):
                    #print(p.get('href'))
                        if p.get('href').endswith('.pdf'):
                            print ('there are some pdf files ', p.get('href'))
                        else: 
                            time.sleep(10)
                            webbrowser.open(p.get('href'))
        
    
    for i in soup.find_all(id ='gs_n'):
        for p in i.find_all('a'):
            url.append(p.get('href'))
            
    set_lis_url_pages = list(set(url))
    set_lis_url_pages.sort()
    print(set_lis_url_pages)
    com_url_pages = []
    for url in set_lis_url_pages:
        link = urllib.parse.urljoin('https://scholar.google.com/', url)
        com_url_pages.append(link)
    #for i in set_lis_url:
    opener(com_url_pages,soup)
    
        #webbrowser.open
    #url =set()
    print('please go to page number {}'.format(page+6))
    
    
while True:
    main(url,page)
    page+=7
    