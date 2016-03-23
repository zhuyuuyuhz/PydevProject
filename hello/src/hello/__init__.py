# -*-coding: utf-8 -*-
import numpy
height = input('height:')
weight = input('weight:')
BMI = ((weight/height)**2)
if BMI < 18.5:
    print "过轻"
elif 18.5 < BMI < 25:
    print "正常"
elif 28 < BMI < 32:
    print "肥胖"
elif BMI > 32:
    print "严重肥胖"