import logging

import requests
import yaml

from api.baseapi import BaseApi
from api.util import Util


class TagApi(BaseApi):
    def __init__(self):
        self.token=Util().token()
        self.params['token']=self.token
        with open('../data/data.yaml',encoding='utf-8') as f:
            self.data =yaml.load(f,Loader=yaml.FullLoader)
    def create_member(self,userid,name,mobile,department=None):
        if department==None:
            department='1'
        self.params['userid']=userid
        self.params['name']=name
        self.params['mobile']=mobile
        self.params['department']=department
        data =self.data['create']
        r=self.request(data)
        print(r.json())
        logging.info('创建成员的响应结果' + repr(r.json()))
        return r.json()["errmsg"]

    def member_get(self,userid):
        self.params['userid']=userid
        data=self.data['get']
        r = self.request(data)
        print(r.json())
        return r.json()

    def member_update(self,userid,name):
        self.params['userid']=userid
        self.params['name']=name
        data=self.data['update']
        r=self.request(data)
        return r.json()["errmsg"]
    def member_delete(self,userid):
        self.params['userid']=userid
        data =self.data['delete']
        r = self.request(data)
        return r.json()["errmsg"]