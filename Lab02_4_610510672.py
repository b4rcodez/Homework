#!/usr/bin/env python3
# สรายุทธ   สมภักดี
# 610510672
# Lab 02
# Problem 4
# 204111 Sec 001

#milliseconds = ms
ms = float(input('Input number of milliseconds: '))
days = ms // 86400000
daysmodulo = ms % 86400000

hours = daysmodulo // 3600000
hoursmodulo = ms % 3600000

minutes = hoursmodulo // 60000
minutesmodulo = ms % 60000

seconds = minutesmodulo // 1000
secondsmodulo = ms % 1000

print('Results = %i'%days,'day(s), %i'%hours,'hour(s), %i'%minutes,'minute(s), %i'%seconds,'second(s), and %i'%secondsmodulo,'millisec(s)')
