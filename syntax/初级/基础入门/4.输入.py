"""
input("提示信息")

- 当程序执行到`input`，等待用户输入，输入完成之后才继续向下执行。
- 在Python中，`input`接收用户输入后，一般存储到变量，方便使用。
- 在Python中，`input`会把接收到的任意用户输入的数据都当做字符串处理。
"""

password = input("请输入你的密码：")
print(f"你的密码是{password}") # 你的密码是123456
print(f"类型是：{type(password)}") # 类型是：<class 'str'>