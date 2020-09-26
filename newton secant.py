# -*- coding: utf-8 -*-
"""
Newton's Method and Secant Method
"""
import math
from math import e

#---------------------------Methods-------------------------------------------#

def newton(p0, f, fprime, tol = .0000001, lim = 25):
    for i in range(0, lim):
        print("", i, " & ", p0, " & ", f(p0))
        p = p0 - (f(p0)/fprime(p0))
        err = p - p0 #if p is 0 for an 1/x function, will cause error
        
        #is this a good enouch approx?
        if (f(p) < tol): 
            return ("pn:", p, ", f(pn):", f(p))
        else:
            p0 = p
            continue
        
    return "Method fails to converge"

def secant(p0, p1, f, tol = .000001, lim = 25):
    for i in range(0, lim):
        print()
        #compute the next p
        p = p1 - ((f(p1)*(p1 - p0))/(f(p1) - f(p0)))
        err = p - p1
        
        if(f(p) < tol): #if error is tolerable, return answer
            return ("pn:", p, ", f(pn):", f(p))
        else: #set the bounds for the next secant
            p0 = p1
            p1 = p
            
    return "Method fails to converge at given limit"


#---------------------------Tests---------------------------------------------#
###Newton's Method example
p0 = (math.pi/4)
def f(x): return (math.cos(x) - x)
def fprime(x): return (-math.sin(x) - 1)
print(newton(p0, f, fprime)) 

###Secant Method example
p0 = .5
p1 = math.pi/4
def f(x): return (math.cos(x) - x)
print(secant(p0, p1, f)) 

