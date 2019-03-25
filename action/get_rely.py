from config.public_data import REQUEST_DATA,RESPONSE_DATA

class GetRelyValue(object):
    # 用于获取接口的依赖数据
    def __init__(self):
        pass
    
    def get(self):
        # 需要获取的数据可能来自上一个接口的请求参数，也可能来自响应body，还有可能来自两者
        pass