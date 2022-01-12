
def login(a,b):
    if a =="admin" and b=="123456":
        return ("登录成功")
    elif a=="" and b=="123456":
        return ("用户名不能为空")
    elif a=="admin" and b=="":
        return ("密码不能为空")
    else:
        return ("登录失败")





