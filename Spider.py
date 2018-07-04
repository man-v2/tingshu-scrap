#!/usr/bin/python
#-*-coding:utf-8-*-

import requests

'''
auto-learning.com 爬虫
'''

class Spider:
    def __init__(self,url):
        self.session = requests.session()
        self.session.get(url)

    def downFile(self):
        print 'test'