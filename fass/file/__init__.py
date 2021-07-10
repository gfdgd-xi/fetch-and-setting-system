import os
# 读取文本文档
def ReadTXT(path: "文件路径")->"读取文本文档":
    f = open(path,"r") # 设置文件对象
    str = f.read() # 获取内容
    f.close() # 关闭文本对象
    return str # 返回结果

# 写入文本文档
def WriteTXT(path: "文件路径", things: "写入内容")->"写入文本文档":
    file = open(path, 'w', encoding='UTF-8') # 设置文件对象
    file.write(things) # 写入文本
    file.close() # 关闭文本对象

# 创建文本文档
def CreateTXT(path: "路径")->"创建文本文档":
    os.mknod(path)