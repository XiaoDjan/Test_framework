"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
在assertion.py中你可以添加更多更丰富的断言，响应断言、日志断言、数据库断言等等，请自行封装。
"""


def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error
