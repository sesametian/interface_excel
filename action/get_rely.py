from config.public_data import REQUEST_DATA,RESPONSE_DATA

class GetRelyValue(object):
    # 用于获取接口的依赖数据
    def __init__(self):
        pass

    @classmethod
    def get(cls,requestData,relyData):
        # 需要获取的数据可能来自上一个接口的请求参数，也可能来自响应body，还有可能来自两者
        if not requestData or not relyData:
            return None
        reData = requestData
        try:
            reData = eval(requestData)  # 将字符串转换成字典类型的对象，以方便调用
        except SyntaxError as err:
            pass

        if relyData:
            relyData = eval(relyData)
        print(type(requestData),type(relyData))

        if isinstance(reData, dict):
            for key,value in relyData.items():
                if key == "request":
                    # 说明依赖的数据来自依赖接口case的请求参数
                    for k,v in value.items():
                        # 切分字符串，获取依赖接口名以及测试用例ID
                        interfaceName,case_id = v.split("->")
                        # 通过嵌套key获取依赖参数的值
                        val = REQUEST_DATA[interfaceName][case_id][k]
                        reData[k] = val
                elif key == "response":
                    for k,v in value.items():
                        interfaceName,case_id = v.split("->")
                        val = RESPONSE_DATA[interfaceName][case_id][k]
                        reData[k] = val
            return reData
        else:
            # 说明请求参数是字符串类型，类似于get请求时直接将参数拼接到url上
            k_v_str = requestData.split("&")
            k_v_dict = {}
            for i in k_v_str:
                key, value = i.split("=")
                k_v_dict[key] = value
            for key, value in relyData.items():
                if key == "request":
                    for k, v in value.items():
                        # 切分字符串，获取依赖接口名以及测试用例ID
                        interfaceName, case_id = v.split("->")
                        # 通过嵌套key获取依赖参数的值
                        val = REQUEST_DATA[interfaceName][case_id][k]
                        k_v_dict[k] = val
                elif key == "response":
                    for k, v in value.items():
                        interfaceName, case_id = v.split("->")
                        if k in RESPONSE_DATA[interfaceName][case_id]:
                            val = RESPONSE_DATA[interfaceName][case_id][k]
                            k_v_dict[k] = val
            requestStr = ""
            for k, v in k_v_dict.items():
                requestStr += k + "=" + v  + "&"
            return requestStr[:-1]

if __name__ == "__main__":
    s = {"username":"","password":""}
    s = "userid=1&password=xdswewe&username=true"
    rely = {"request":{"username":"用户注册->1","password":"用户注册->1"}}
    print(GetRelyValue.get(str(s), str(rely)))