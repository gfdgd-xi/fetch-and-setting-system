import time
import datetime
import calendar

def FormatTime()->"返回已经格式化后的时间":
    return datetime.now()

def YearMini()->"返回年份的后两位（0~99），如21":
    return datetime.datetime.now().strftime("%y")

def YearFull()->"返回年份（0~9999），如2021":
    return datetime.datetime.now().strftime("%Y")

def Month()->"返回月份（1~12），如7":
    return datetime.datetime.now().strftime("%m")

def DayInMonth()->"返回日期在一个月里（0~28/29/30/31），如8":
    return datetime.datetime.now().strftime("%d")

def DayInYear()->"返回日期在一年里（0/365/366），如189":
    return datetime.datetime.now().strftime("%j")

def HourOf24Method()->"返回小时（二十四小时计时法）（0~24），如11":
    return datetime.datetime.now().strftime("%H")

def HourOf12Method()->"返回小时（十二小时计时法）（0~12），如11":
    return datetime.datetime.now().strftime("%I")

def Minute()->"返回分钟（0~60），如5":
    return datetime.datetime.now().strftime("%M")

def Second()->"返回秒（0~60），如59":
    return datetime.datetime.now().strftime("%S")

def TimeZone()->"返回时区，如CST":
    #return datetime.datetime.now().strftime("%Z")
    return time.strftime("%Z", time.localtime())

def AMOrPM()->"返回单位（AM/PM），如AM":
    return datetime.datetime.now().strftime("%p")

def MonthFullString()->"返回月份的全称，如July":
    return datetime.datetime.now().strftime("%B")

def MonthMiniString()->"返回月份的简称，如Jul":
    return datetime.datetime.now().strftime("%b")

def WeekFullString()->"返回星期的全称，如Thursday":
    return datetime.datetime.now().strftime("%A")

def WeekMiniString()->"返回星期的简称，如Thu":
    return datetime.datetime.now().strftime("%a")

def MonthCalendar(year: "年份", month: "月份")->"返回指定日期所对应的月历":
    return calendar.month(year, month)

def DayInWeek(year: "年份", month: "月份", day: "日期")->"返回星期（从星期一开始）":
    return calendar.weekday(year, month, day) + 1

def Week()->"返回星期（从星期一开始）":
    return datetime.datetime.now().strftime("%w")