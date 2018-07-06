#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
import os
import sys
import json

'''
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串 
'''

class AutoLearning:

    def __init__(self, url):
        print('autolearing')
        self.session = requests.session()
        self.session.get(url, verify=False)

    def type_link(self):
        url = 'https://api.auto-learning.com/v3/xcx/type-link?sessionId=undefined&pageIndex=0'
        res = self.session.get(url)
        self.write_txt_file('D:\docs\Dev\Python\Code\\tingshu-scrap\\type-link.txt', res.content)
        #
        # json_data = res.content
        # print(json_data)
        # print(type(json_data))
        # dict_data = json.loads(json_data)
        # print(dict_data['meta']['enMessage'])

    def write_txt_file(self, path, content):
        with open(path, 'w') as file:
            file.write(content)

if __name__ == '__main__':
    obj = AutoLearning('https://api.auto-learning.com')
    obj.type_link()