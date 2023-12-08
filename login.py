import openi


def login_with_token(token):
    openi.login(token=token)


login_with_token("你的令牌")

from openi.dataset import upload_file

upload_file("你的文件路径", "仓库地址", "gpu")
