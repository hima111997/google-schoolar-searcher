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
        
        '''openning the the researches in the first page'''
        
        for i in soup.find_all(id ='gs_res_ccl_mid'):
            for p in i.find_all('a'):
                if p.get('href').startswith('http'):
                    #print(p.get('href'))
                    if p.get('href').endswith('.pdf'):
                        print ('\nthere are some pdf files\n ', p.get('href')) # prints the link for PDFs
                    else: 
                        time.sleep(5)
                        webbrowser.open(p.get('href')) 
        
        '''openning the rest of pages upob user request'''
        for i in com_url_pages:
            open_next = input('do you want to see the next page?\n\
1 for yes\n\
2 for no\n')
            if open_next =='1':
                pass
            elif open_next =='2':
                return open_next
            r = requests.get(i).text
            soup = BeautifulSoup(r,'html.parser')
            #print(com_url_pages)
            for i in soup.find_all(id ='gs_res_ccl_mid'):
                for p in i.find_all('a'):
                    if p.get('href').startswith('http'):
                    #print(p.get('href'))
                        if p.get('href').endswith('.pdf'):
                            print ('\nthere are some pdf files\n ', p.get('href'))
                        else: 
                            time.sleep(5)
                            webbrowser.open(p.get('href'))
        
    ''' find and create a list of pages URL'''
    for i in soup.find_all(id ='gs_n'):
        for p in i.find_all('a'):
            url.append(p.get('href'))
            
    set_lis_url_pages = list(set(url))
    set_lis_url_pages.sort() # this list contains the URL pages (not complete URLs)
    #print(set_lis_url_pages)
    com_url_pages = []
    
    '''creating the full URL address'''
    for url in set_lis_url_pages:
        link = urllib.parse.urljoin('https://scholar.google.com/', url)
        com_url_pages.append(link)
    #for i in set_lis_url:
    open_next = opener(com_url_pages,soup)
    return open_next
    
       
    
while True:
    open_next = main(url,page)
    page+=7
    print(open_next)
    if open_next == '2':
        break
    