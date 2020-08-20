import re
from api.weixinapi import TagApi
import pytest


def data():
    data =[('Hogwarts_0'+str(x),'霍格沃兹0'+str(x),'138%08d'%x) for x in range(5)]
    return data
class TestApiMembers:
    @pytest.mark.parametrize('usr_id,name,phone', data())
    def test_member(self,usr_id, name, phone):
        try:
            assert "created" in TagApi().create_member(usr_id, name, phone)
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                TagApi().member_delete(re_userid)
        assert name in TagApi().member_get(usr_id)["name"]
        assert "updated" in TagApi().member_update(usr_id, '霍格沃兹1')
        assert '霍格沃兹1' in TagApi().member_get(usr_id)["name"]
        assert "deleted" in TagApi().member_delete(usr_id)
        assert 60111 == TagApi().member_get(usr_id)["errcode"]


