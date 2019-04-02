# 专门用于做数据依赖存储处理
from config.public_data import RESPONSE_DATA,REQUEST_DATA

class RelyDataStore(object):
    def __init__(self):
        pass
    @classmethod
    def do(cls, apiName, caseId , requestData, responseBody, dataStore):
        param_dict = {}
        if isinstance(requestData, str):
            p_list = requestData.split("&")
            for i in p_list:
                key,value = i.split("=")
                param_dict[key] = value
            requestData = param_dict
        for key, value in dataStore.items():
            if key == "request":
                # 说明需要存储的数据是来自于接口的请求参数
                for i in value:
                    if i in requestData:
                        if apiName not in REQUEST_DATA:
                            REQUEST_DATA[apiName] = {str(caseId): {i:requestData[i]}}
                        else:
                            if str(caseId) in REQUEST_DATA[apiName]:
                                REQUEST_DATA[apiName][str(caseId)][i] = requestData[i]
                            else:
                                REQUEST_DATA[apiName][str(caseId)] = {i:requestData[i]}
            elif key == "response":
                # 说明需要存储的依赖数据是来自接口的响应body
                for j in value:
                    if j in responseBody:
                        if not apiName in RESPONSE_DATA:
                            RESPONSE_DATA[apiName] = {str(caseId):{j:responseBody[j]}}
                        else:
                            if str(caseId) in RESPONSE_DATA[apiName]:
                                RESPONSE_DATA[apiName][str(caseId)][j] = responseBody[j]
                            else:
                                RESPONSE_DATA[apiName][str(caseId)] = {j:responseBody[j]}
                    else:
                        print("需要存储的依赖参数%s在响应body中未找到" %j)

if __name__ == '__main__':
    r = {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}
    # r =  'username=sdfwe&password=xdswewe&flag=true'
    s = {"request":["username","password"],"response":["userid"]}
    res = {"userid":12,"code":"00"}
    RelyDataStore.do("register",1, r, res, s)
    print(REQUEST_DATA)
    print(RESPONSE_DATA)
