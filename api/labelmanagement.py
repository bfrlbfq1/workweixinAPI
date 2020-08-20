import yaml

from api.baseapi import BaseApi
from api.util import Util


class LabelManagement(BaseApi):
    """标签管理"""
    def __init__(self):
        self.token =Util().token()
        self.params['token'] = self.token
        with open('../data/labeldata.yaml', encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
    def create_label(self,tagname,tagid):
        '''创建标签'''
        self.params['tagname']=tagname
        self.params['tagid']=tagid
        data=self.data['create']
        r=self.request(data)
        return r.json()
    def update_label(self,tagname,tagid):
        '''更新标签'''
        self.params['tagname']=tagname
        self.params['tagid']=tagid
        data=self.data['update']
        r=self.request(data)
        return r.json()

    def get_label(self,tagid):
        '''获取标签成员'''
        self.params['tagid']=tagid
        data=self.data['get']
        r=self.request(data)
        return r.json()
    def delete_label(self,tagid):
        '''删除标签成'''
        self.params['tagid']=tagid
        data=self.data['delete']
        r=self.request(data)
        return r.json()

