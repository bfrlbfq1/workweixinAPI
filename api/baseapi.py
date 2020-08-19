import json

import requests


class BaseApi:
    params={}
    def request(self,data):
        row =json.dumps(data)
        for key,value in self.params.items():
            row=row.replace("${"+key+"}",value)
        data=json.loads(row)
        r=requests.request(**data)
        return r