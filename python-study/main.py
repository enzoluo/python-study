from utils import HttpClientUtil
from utils.sqllite_operate import Sqllite_Util
import json
if __name__ == "__main__":
    # res = HttpClientUtil.send_get("https://program.tywork.top:9065/mina/index")
    user = dict(name='yingzheng', age=11)
    # res = HttpClientUtil.send_post_json("http://localhost:8891/getUser", user)
    person = {"name": (None, "萌娃"), "password": (None, "****")}
    user = {"name": "jibo", "password": "123"}
    params = {}
    params["province"] = "11"
    params["city"] = "1101"
    params["county"] = "110102"
    params["year"] = "1988"
    params["month"] = "12"
    params["day"] = "06"
    params["sex"] = "%E7%94%B7"
    params["num"] = "10"
    url = "https://www.uihtm.com/idcard/"
    res = HttpClientUtil.send_post_form_data(url, params)
    all_list = json.loads(res)['data']['all_list']
    obj = Sqllite_Util()
    for item in all_list:
        item = item.replace(' ', '-', 2).replace(' ', '')
        sort, name, idcard = item.split('-')
        obj.insert('data_user','user_name,id_card',"'%s','%s'" % (name,idcard))
    print(1)