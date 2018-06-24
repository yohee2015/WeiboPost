#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:star 
@file: weiboPost.py 
@time: 2018/06/24
"""
import random
import re
import time

import requests
from config import *


class SendWeiboMsg():
    def __init__(self):
        self.postUrl = 'https://weibo.com/p/aj/proxy?ajwvr=6&__rnd=1529828922439'
        self.zfUrl = 'https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100306&__rnd=1529822846081'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'weibo.com',
            'Origin': 'https://weibo.com',
            'Referer': 'https://weibo.com/u/1669879400?is_all=1',
            'X-Requested-With': 'XMLHttpRequest'
        }

        self.cookies = {
            'Cookie': 'SINAGLOBAL=2595098081165.772.1528019870909; login_sid_t=b17543f101602a5e43570143a55f88ae; cross_origin_proto=SSL; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; TC-V5-G0=40eeee30be4a1418bde327baf365fcc0; wb_view_log=1280*10241; _s_tentry=www.baidu.com; UOR=,,www.baidu.com; Apache=6901247442331.131.1529814105269; ULV=1529814105278:11:11:2:6901247442331.131.1529814105269:1529812994719; SSOLoginState=1529814105; SCF=At74JyOmfjXj3ufUlUIhEkxKlQOSdsuwMg3H25ozlX-eK4ynGMe0wOYInmGih350KAFQlA8J12DmViDnMS8TRb0.; SUB=_2A252K2wJDeRhGeNL41IS8SnIyziIHXVVQdrBrDV8PUNbmtAKLRSskW9NSC6L22qFeWeeB08k_Q8Bef2NTTwcDvlt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5sEMYmfjmgcWY1qhONLzeq5JpX5K2hUgL.Fo-f1h50eKMXehB2dJLoI0i29g8ETCH8SE-ReEHWxFH8SCHFSEHFSFH8SCHFeF-RxbH8SE-4SF-4BEH8SCHFxb-Re7tt; SUHB=06Z1Vh1SgW9Q7R; ALF=1561350104; un=yohee2015@sina.com; wvr=6; TC-Page-G0=0dba63c42a7d74c1129019fa3e7e6e7c'
        }
    '''
    超话发博
    '''
    def sendMsg(self,msg):
        postData = {
            'location': 'page_100808_super_index',
            'text': msg,
            # 'style_type:1',
            # 'pic_id':'0065Ertqgy1fsm9hcj51tj30sg0ppn5y|0065Ertqgy1fsm9hbkciuj30j60dqmz4|0065Ertqgy1fsm9hdewoyj30sg175h3q',
            'pdetail': '100808237347456f0169aa3c4843505d877bc2',
            'isReEdit': 'false',
            'sync_wb': '1',
            'pub_source': 'page_1',
            'api': 'http://i.huati.weibo.com/pcpage/operation/publisher/sendcontent?sign=super&page_id=100808237347456f0169aa3c4843505d877bc2',
            'object_id': '1022:100808237347456f0169aa3c4843505d877bc2',
            'module': 'publish_913',
            'page_module_id': '913',
            'longtext': '1',
            'topic_id': '1022:100808237347456f0169aa3c4843505d877bc2',
            'pub_type': 'dialog',
            '_t': '0'
        }
        html = requests.post(self.postUrl, data=postData, cookies=self.cookies, headers=self.headers)
        print(time.strftime('%Y-%m-%d %H:%M:%S'), html.text)

    def zfMsg(self, mid, msg):
        zfData = {
            'mid': mid,
            'style_type': '1',
            'reason': msg,
            'location': 'page_100306_home',
            'pdetail': '1003061669879400',
            'is_comment_base': '1',
            'rank': '0',
            'isReEdit': 'false',
            '_t': '0'
        }
        html = requests.post(self.zfUrl, data=zfData, cookies=self.cookies, headers=self.headers)
        code = html.json()['code']
        print(code, time.strftime('%Y-%m-%d %H:%M:%S'), msg)
        return code


if __name__ == '__main__':
    sendWeiboMsg = SendWeiboMsg()
    for i in range(TODAY_TARGET_COUNT):
        msg = random.choice(MESSAGE)
        mid = random.choice(MID_LIST)
        code = sendWeiboMsg.zfMsg(mid, msg)
        if code != '100000':
            print('出错了！')
            print('发布失败，休息10分钟再继续！', code, time.strftime('%Y-%m-%d %H:%M:%S'), msg)
            time.sleep(600)
        time.sleep(random.randint(180, 480))
