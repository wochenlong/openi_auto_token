# openi_auto_token

参考文档：https://openi.pcl.ac.cn/docs/index.html#/api/intro

不需要盲输，自动输入您的token

————————————————————————————————


import openi


def login_with_token(token):
    openi.login(token=token)


login_with_token("你的令牌")

from openi.dataset import upload_file

upload_file("你的本地文件路径", "仓库地址", "gpu")
