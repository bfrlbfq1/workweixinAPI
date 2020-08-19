import logging

import pytest
import requests


class Util:
    @pytest.fixture(scope='session')
    # def token(self,tmp_path_factory,worker_id):
    def token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        param = {
            'corpid': 'wwd2f2c19220c60028',
            'corpsecret': 'z9vT6s5B9FOq00rjoGudhjk77Eva56izk-SyhvqWqlo'
        }
        r = requests.get(url, params=param)
        logging.info('获取的access_token' + repr(r.json()))
        return r.json()["access_token"]