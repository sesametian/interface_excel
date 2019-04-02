# 此文件主要用于处理接口发送请求并返回响应结果
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    @classmethod
    def request(cls,requestUrl,requestMethod,paramsType,requestData = None,headers = None):
        if requestMethod == "post":
            if paramsType == "form":
                # 说明接口传参方式为表单提交，通过data变量接收
                response = requests.post(url = requestUrl,data = json.dumps(requestData),headers = headers)
                return response
            elif paramsType == "json":
                # 说明接口传参方式为json，通过json变量接收
                response = requests.post(url=requestUrl, json=json.dumps(requestData), headers=headers)
                return response
        elif requestMethod == "get":
            if paramsType == "url":
                # 说明接口的请求参数是直接拼接在url上的
                request_url = "%s%s" %(requestUrl, requestData)
                response = requests.get(url=request_url, headers=headers)
            elif paramsType == "params":
                # 说明接口的get请求传参是通过params参数接收的
                if isinstance(requestData, dict):
                    response = requests.get(url=requestUrl, params=json.dumps(requestData), header=headers)
                else:
                    response = requests.get(url=requestUrl, params=requestData)
                return response

if __name__ == "__main__":
    requestUrl = "http://39.106.41.11:8080/register/"
    requestMethod = "post"
    paramsType = "form"
    requestData = {"username":"xxxe23sd", "password":"dflwe23sd", "email":"wcx@qq.com"}
    response = HttpClient.request(requestUrl, requestMethod, paramsType, requestData)
    print(response.status_code)
    print(response.json())