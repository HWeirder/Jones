# -*- coding: utf-8 -*-

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import requests
import json
import re

global_page_url = 'https://www.dytt8.net/index2.htm'


def spider():
    page_data = requests.get(global_page_url)
    print(page_data.body)


if __name__ == '__main__':
    print("电影天堂爬虫 ", global_page_url)
    spider()
