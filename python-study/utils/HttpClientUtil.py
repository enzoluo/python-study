import requests
import json


def send_get(url):
    return requests.get(url).text


# 发送 json参数的POST请求
def send_post_json(url: str, params: dict):
    data = json.dumps(params)
    headers = {'Content-Type': 'application/json'}
    return requests.post(url, data=data, headers=headers).text


# 发送 form-data参数的POST请求
def send_post_form_data(url, params: dict):
    # 发送 form-data 注意项有两点
    # 1、form-data参数要写成如下格式，注意有None
    # 2、此种方式发送form-data类型参数时，请求时不要headers，且用files参数
    form_data = {}
    for key in params:
        form_data[key] = (None, params[key])
    return requests.request("POST", url, files=form_data).text
