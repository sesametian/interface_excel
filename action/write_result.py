from config.public_data import *

def write_result(wbObj, sheetObj, responseBody,errorKey, rowNo):
    # 将测试结果写到excel中对应的单元格中
    # 写响应body
    wbObj .writeCell(sheet=sheetObj, content="%s" %responseBody,
                     rowNo=rowNo, colsNo=CASE_responseData)
    # 写校验结果状态列及错误
    if errorKey:
        wbObj.writeCell(sheet=sheetObj, content="faild",
                        rowNo=rowNo, colsNo=CASE_status)
        wbObj.writeCell(sheetObj, content="%s" %errorKey, rowNo=rowNo,
                        colsNo=CASE_errorInfo)
    else:
        wbObj.writeCell(sheet=sheetObj, content="pass",
                        rowNo=rowNo, colsNo=CASE_status)