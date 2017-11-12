# -*- coding: UTF-8 -*-
import requests
import lxml
from bs4 import BeautifulSoup 
# FT中文 首页内容
ft = requests.get('http://www.ftchinese.com/')
source = BeautifulSoup(ft.text,"lxml");
# 获取头条文章链接
article = source.find('div',class_="XL8").find('a',class_='item-headline-link')['href']
# 每日头条文章 全文模式
newFt = requests.get('http://www.ftchinese.com'+article,params={'full':'y'})
newSource = BeautifulSoup(newFt.text,"lxml");
# 获取文章链接，标题，副标题，内容
url = newFt.url
title = newSource.find('h1',class_='story-headline').get_text()
subtitle = newSource.find('div',class_='story-lead').get_text()
articlecontent = newSource.find('div',class_='story-body').find_all('p')
print url,title.encode('utf-8'),subtitle.encode('utf-8')
body = []
for index in articlecontent:
   body.append(index.get_text())
   print index.get_text().encode('utf-8')
