"""
使用接口进行成员的创建，获取、更新、删除

"""
import json
import logging
import re

import pytest
import requests

def data():
    data =[('Hogwarts_0'+str(x),'霍格沃兹0'+str(x),'138%08d'%x) for x in range(20)]
    return data
class TestMembers:
    '''获取token'''
    logging.basicConfig(level=logging.INFO)
    @pytest.fixture(scope='session')
    # def token(self,tmp_path_factory,worker_id):
    def token(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        param={
            'corpid':'wwd2f2c19220c60028',
            'corpsecret':'z9vT6s5B9FOq00rjoGudhjk77Eva56izk-SyhvqWqlo'
        }
        r=requests.get(url,params=param)
        logging.info('获取的access_token'+repr(r.json()))
        return r.json()["access_token"]
        # if not worker_id:
        #     return get_token()
        # root_tmp_dir =tmp_path_factory.getbasetemp().parent
        # fn=root_tmp_dir/"date.json"
        # with FileLock(str(fn)+'.lock'):
        #     if fn.is_file():
        #         data=json.loads(fn.read_text())
        #     else:
        #         data =get_token()
        #         fn.write_text(json.dumps(data))
        # return data
    def create_member(self,token,userid,name,mobile,department=None):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
        if department==None:
            department=[1]
        data={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        r= requests.post(url,json=data)
        print(r.json())
        logging.info('创建成员的响应结果' + repr(r.json()))
        return r.json()["errmsg"]

    def member_get(self,token,userid):
        url='https://qyapi.weixin.qq.com/cgi-bin/user/get'
        param={
            "access_token":token,
            "userid":userid
        }
        r=requests.get(url,params=param)
        print(r.json())
        return r.json()

    def member_update(self,token,userid,name):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}'
        data={
            "userid": userid,
            "name": name,
        }
        r =requests.post(url,json=data)
        return r.json()["errmsg"]
    def member_delete(self,token,userid):
        url='https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        param={
            "access_token":token,
            "userid":userid
        }
        r= requests.get(url,params=param)
        return r.json()["errmsg"]
    @pytest.mark.parametrize('usr_id,name,phone',data())
    def test_member(self,token,usr_id,name,phone):
        # usr_id='Hogwarts_01'
        try:
            assert "created" in self.create_member(token,usr_id,name,phone)
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid=re.findall(":(.*)'$",e.__str__())[0]
                self.member_delete(token,re_userid)
        assert name in self.member_get(token,usr_id)["name"]
        assert "updated" in self.member_update(token,usr_id,'霍格沃兹1')
        assert '霍格沃兹1' in self.member_get(token, usr_id)["name"]
        assert "deleted" in self.member_delete(token,usr_id)
        assert 60111 == self.member_get(token, usr_id)["errcode"]

