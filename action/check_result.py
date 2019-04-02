# 此文件主要用于接口响应结果的检测
import re

class CheckResult(object):
    def __init__(self):
        pass

    @classmethod
    def check(cls, responseBody, checkPoint):
        errorKey = {}
        for key,value in checkPoint.items():
            if isinstance(value, str):
                # 说明是等值校验
                if responseBody[key] != value:
                    errorKey[key] = responseBody[key]
            elif isinstance(value, dict):
                # 说明是需要通过正则或类型做模糊校验
                sourceData = responseBody[key] #接口实际返回的值
                if "type" in value:
                    # 说明是校验数据类型
                    typeS = value["type"]
                    if typeS == "N":
                        # 说明是校验整数类型
                        if not isinstance(sourceData, int):
                            errorKey[key] = sourceData
                elif "value" in value:
                    # 说明需要通过正则表达式去模糊校验
                    regStr = value["value"]
                    rg = re.match(regStr, "%s" %sourceData)
                    if not rg:
                        errorKey[key] = sourceData
        return errorKey

if __name__ == "__main__":
    r = {"code": "01", "userid": 12, "id": "1a2"}
    c = {"code": "00", "userid": {"type": "N"}, "id": {"value": "\d+$"}}
    print(CheckResult.check(r, c))