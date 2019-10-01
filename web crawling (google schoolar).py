# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:02:36 2019

@author: mohamed
"""
import requests, webbrowser,urllib
from bs4 import BeautifulSoup

url = set()
page = 10
def main(url,page):
    
    user_input= input('please enter the google schooler URL: ')
    r = requests.get(user_input).text
    soup = BeautifulSoup(r,'html.parser')
    for i in soup.find_all(id ='gs_n'):
        print (i)
        for p in i.find_all('a'):
            if p.get('href') in url:
                
                continue
            else:
                print(p.get('href'))
                url.add(p.get('href'))
   
    #url2 = url2.union(url)
    #print(set(url2))
    print(url)
    #print (url2)
    for i in url:
        webbrowser.open(urllib.parse.urljoin('https://scholar.google.com/', i))
    #url =set()
    print('please go to page number {}'.format(page+6))
    
    '''openening the first 10 files in a google schoolar Url'''
    
    '''for i in soup.find_all(id ='gs_res_ccl_mid'):
        for p in i.find_all('a'):
            if p.get('href').startswith('http'):
                #print(p.get('href'))
                if p.get('href').endswith('.pdf'):
                    print ('there are some pdf files ', p.get('href'))
                else:    
                    webbrowser.open(p.get('href'))'''
while True:
    main(url,page)
    page+=7