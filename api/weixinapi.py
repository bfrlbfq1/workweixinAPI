import logging

import requests
import yaml

from api.baseapi import BaseApi
from api.util import Util


class TagApi(BaseApi):
    def __init__(self):
        self.token=Util().token()
        self.params['token']=self.token
    def create_member(self,userid,name,mobile,department=None):
        if department==None:
            department='1'
        # data={
        #     "method":"post",
        #     "url":f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',
        #     "json":{
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department,
        #     }
        # }
        self.params['userid']=userid
        self.params['name']=name
        self.params['mobile']=mobile
        self.params['department']=department
        with open('../data/data.yaml',encoding='utf-8') as f:
            data =yaml.safe_load(f)['create']
        r=self.request(data)
        print(r.json())
        logging.info('创建成员的响应结果' + repr(r.json()))
        return r.json()["errmsg"]

    def member_get(self,userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            "params": {
                "access_token":self.token,
                "userid":userid
            }
        }
        r = self.request(**data)
        print(r.json())
        return r.json()

    def member_update(self,userid,name):
        data={
            "method":"post",
            "url":f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}',
            "json":{
                "userid": userid,
                "name": name,
            }
        }
        r=self.request(**data)
        return r.json()["errmsg"]
    def member_delete(self,userid):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        r = self.request(**data)
        return r.json()["errmsg"]