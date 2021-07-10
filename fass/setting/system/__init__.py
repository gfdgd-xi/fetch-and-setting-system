##########################
# 作者：gfdgd xi
##########################
from fass.information import *
import platform
import subprocess

# 用途：运行系统命令并返回运行的返回值
# 适用平台：Windows、Linux
def RunCommand(command: "要运行的命令")->"返回的是运行的返回值":
    return subprocess.getoutput(command)

# 用途：关机
# 适用平台：Windows、Linux
def CloseComputer()->"关闭计算机":
    if IsLinux:  # 判断系统平台
        RunCommand("poweroff")         # 如果是 Linux，调用命令“poweroff”
    else:                              # 否则就是 Windows
        RunCommand("shutdown -s -t 0") # 调用命令“shutdown -s -t 0”

# 用途：重启
# 适用平台：Windows、Linux
def RestartComputer()->"重启计算机":
    if IsLinux:  # 判断系统平台
        RunCommand("reboot")           # 如果是 Linux，调用命令“reboot”
    else:                              # 否则就是 Windows
        RunCommand("shutdown -r -t 0") # 调用命令“shutdown -r -t 0”

#####################################
# 控制进程
#####################################
# 用途：使用 PID 杀死进程
# 适用平台：Windows、Linux
def RestartComputer(PID: "PID",forceCloseProgress: "强制杀死进程"=False)->"通过进程名称杀死进程":
    if IsLinux:  # 判断系统平台
        # 如果是 Linux
        if forceCloseProgress: # 判断是否强制杀死进程
            RunCommand("kill -9 '{}'".format(PID))  # 如果是，调用命令“killall -9 XXX”
            return
        RunCommand("kill '{}'".format(PID))    # 否则“killall XXX”
    else:                              # 否则就是 Windows
        if forceCloseProgress: # 判断是否强制杀死进程
            RunCommand("taskkill /f /pid '{}'".format(PID))  # 如果是，调用命令“killall -9 XXX”
            return
        RunCommand("taskkill /pid '{}'".format(PID)) # 否则调用命令“taskkill /im XXX”

# 用途：使用进程名称杀死进程
# 适用平台：Windows、Linux
def RestartComputer(progressName: "进程名称",forceCloseProgress: "强制杀死进程"=False)->"通过进程名称杀死进程":
    if IsLinux:  # 判断系统平台
        # 如果是 Linux
        if forceCloseProgress: # 判断是否强制杀死进程
            RunCommand("killall -9 '{}'".format(progressName))  # 如果是，调用命令“killall -9 XXX”
            return
        RunCommand("killall '{}'".format(progressName))    # 否则“killall XXX”
    else:                              # 否则就是 Windows
        if forceCloseProgress: # 判断是否强制杀死进程
            RunCommand("taskkill /f /im '{}'".format(progressName))  # 如果是，调用命令“killall -9 XXX”
            return
        RunCommand("taskkill /im '{}'".format(progressName)) # 否则调用命令“taskkill /im XXX”