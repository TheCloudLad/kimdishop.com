# # Tamplate Injaction Tool 
# # Created by Cloud_Lad & ILZFE


import requests
import wget
import urllib.request
from bs4 import BeautifulSoup
from colorama import Fore , Back
from colorama import init as colorama_init
from time import sleep
import datetime


colorama_init(autoreset=True)

def Web_Scraper():
    _Proxy_ = {
        'proxy' : 'http://45.92.108.112:8080'
    }
    _Url_ = 'https://kimdishop.com/wp-content/uploads/fsqm-files/'
    _Requst_ = requests.get(_Url_,proxies=_Proxy_)
    _Soup_ = BeautifulSoup(_Requst_.text, 'html.parser')
    _Urls_ = []
    for link in _Soup_.find_all('a'):
        _href_ = (link.get('href'))
        _Apended_ = (f"https://kimdishop.com/wp-content/uploads/fsqm-files/{_href_}")
        _File_ = open("Link.txt","a")
        _Formated_ = _File_.write(_Apended_ + "\n")


Web_Scraper()