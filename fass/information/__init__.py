import psutil
import socket
import platform
######################################################
#
# 硬件
#
######################################################
# 用途：检测CPU生产厂家
# 适用平台：Windows、Linux
def CPUMachine()->"CPU生产厂家":
    return platform.machine()

def CPUUsage()->"CPU使用率":
    return psutil.cpu_percent()

def MemoryUsage()->"内存使用率":
    phymem = psutil.virtual_memory()
    return phymem.percent

def VirtualMemoryAllVolume()->"虚拟内存全部的量（MB）":
    phymem = psutil.virtual_memory()
    return phymem.total / 1024 / 1024

def MemoryUsedVolume()->"内存已经使用的量（MB）":
    phymem = psutil.virtual_memory()
    return phymem.total / 1024 / 1024

######################################################
#
# 软件
#
######################################################

##########################
# 系统
##########################
# 用途：检测运行平台
# 适用平台：Windows、Linux
def ProgramRunSystem()->"系统名称":
    return platform.system()

# 用途：判断运行平台是不是Linux
# 适用系统：Windows、Linux
def IsLinux()->"判断平台是不是 Linux，返回 bool":
    if ProgramRunSystem().lower() == "Linux".lower():
        return True
    return False

##########################
# 网络
##########################
def HostName()->"获取计算机名":
    return socket.gethostname()

def IPAddress()->"获取计算机IP地址":
    return socket.gethostbyname(HostName)