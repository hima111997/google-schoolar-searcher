# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:02:36 2019

@author: mohamed
"""
import requests, webbrowser,urllib, time
from bs4 import BeautifulSoup

url = []
opened_pages = []
page = 10



def main(url,page): 
    
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
        
        '''openning the rest of pages upon user request'''
        page_number = 2
        for i in com_url_pages:
            open_next = input('do you want to see the next page (page: {})?\n\
1 for yes\n\
2 for no\n'.format(page_number))
            if open_next =='1':
                page_number+=1
                pass
            elif open_next =='2':
                return open_next
            r = requests.get(i).text
            soup = BeautifulSoup(r,'html.parser')
            
            for i in soup.find_all(id ='gs_res_ccl_mid'):
                for p in i.find_all('a'):
                    if p.get('href').startswith('http'):
                    
                        if p.get('href').endswith('.pdf'):
                            print ('\nthere are some pdf files\n ', p.get('href'))
                        else: 
                            time.sleep(5)
                            webbrowser.open(p.get('href'))
        
    ''' find and create a list of pages URL'''
    user_input= input('please enter the google schooler URL: ')
    r = requests.get(user_input).text
    soup = BeautifulSoup(r,'html.parser')
    
    num_pages = int(input('for what page you want to see the results: '))
    
    if num_pages == 1:
        for i in soup.find_all(id ='gs_res_ccl_mid'):
            for p in i.find_all('a'):
                if p.get('href').startswith('http'):
                    #print(p.get('href'))
                    if p.get('href').endswith('.pdf'):
                        print ('\nthere are some pdf files\n ', p.get('href')) # prints the link for PDFs
                    else: 
                        time.sleep(5)
                        webbrowser.open(p.get('href'))
        return 1
        
    if 1 < num_pages <= 10:
        for i in soup.find_all(id ='gs_n'):
            #print (i)
            for p in i.find_all('a'):
                url.append(p.get('href'))
                
        set_lis_url_pages = list(set(url))
        set_lis_url_pages.sort() # this list contains the URL pages (not complete URLs)
        
        com_url_pages = []
        for num in range(num_pages-1):
            link = urllib.parse.urljoin('https://scholar.google.com/', set_lis_url_pages[num])
            com_url_pages.append(link)
    '''creating the full URL address'''
    '''update:  showing only a specific number of pages'''
        
            
        
    
    
    if num_pages > 10:
        for i in soup.find_all(id ='gs_n'):
            #print (i)
            for p in i.find_all('a'):
                url.append(p.get('href'))
                
        set_lis_url_pages = list(set(url))
        set_lis_url_pages.sort() # this list contains the URL pages (not complete URLs)
        com_url_pages = []
        for num in range(len(set_lis_url_pages)):
            link = urllib.parse.urljoin('https://scholar.google.com/', set_lis_url_pages[num])
            com_url_pages.append(link)
        
        #print(com_url_pages, len(com_url_pages))
        
        repetitions = (num_pages - 10)/4
        if int(repetitions) < repetitions:
            repetitions = int(repetitions) + 1
        #print (repetitions)
        for i in range(repetitions):            
            r = requests.get(com_url_pages[-1]).text
            soup_10 = BeautifulSoup(r,'html.parser')
            after_10 = []
            
            for i in soup_10.find_all(id ='gs_n'):
            #print (i)
                for p in i.find_all('a'):
                    after_10.append(p.get('href'))
                    #print (p.get('href'))
                for url in range(len(after_10)):
                    link = urllib.parse.urljoin('https://scholar.google.com/', after_10[url])
                    if link not in com_url_pages:
                        com_url_pages.append(link)
                    else:
                        continue
        com_url_pages = list(set(com_url_pages))
        '''future update:
            1- creating dict containing the part of the url that indicates the page number (key), url(value)
            2- creating list having only the keys sorted
            3- modifiying the original list com_url_pages so that its pages are ordered'''
        #removal = len(com_url_pages) - num_pages + 1
        
        #for i in range(removal):
         #   del(com_url_pages[-1])
        
        open_next = opener(com_url_pages,soup)
    open_next = opener(com_url_pages,soup)
    return open_next
    
       
    
while True:
    open_next = main(url,page)
    page+=7
    #print(open_next)
    if open_next == '2':
        break
    