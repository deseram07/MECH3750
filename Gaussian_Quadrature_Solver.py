"""
This program uses Gaussian Quadrature to integrate between the specified 
points.

Author: Buddhika De Seram
Student ID: 42229904
"""

import numpy as np
import sys

"""
Node (r) and weights (c) for the interval [-1,1]
""" 
r2 = [np.sqrt(3.0)/3.0, -np.sqrt(3.0)/3.0]
r3 = [np.sqrt(3.0/5.0),0.0,-np.sqrt(3.0/5.0)]
r4 = [np.sqrt((3.0+(2.0*np.sqrt(6.0/5.0)))/7.0),np.sqrt((3.0-(2.0*np.sqrt(6.0/5.0)))/7.0),
      -np.sqrt((3.0-(2.0*np.sqrt(6.0/5.0)))/7.0),-np.sqrt((3.0+(2.0*np.sqrt(6.0/5.0)))/7.0)]
r5 = [np.sqrt(5.0+(2.0*np.sqrt(10.0/7.0)))/3.0,np.sqrt(5.0-(2.0*np.sqrt(10.0/7.0)))/3.0,0.0,
      -np.sqrt(5.0-(2.0*np.sqrt(10.0/7.0)))/3.0,-np.sqrt(5.0+(2.0*np.sqrt(10.0/7.0)))/3.0]

c2 = [1.0,1.0]
c3 = [5.0/9.0, 8.0/9.0, 5.0/9.0]
c4 = [(18.0-np.sqrt(39.0))/36.0, (18.0+np.sqrt(39.0))/36.0,(18.0+np.sqrt(39.0))/36.0,(18.0-np.sqrt(39.0))/36.0]
c5 = [(322.0-13.0*(np.sqrt(70.0)))/900.0,(322.0+13.0*(np.sqrt(70.0)))/900.0,float(128.0)/float(225.0), 
      (322.0+13.0*(np.sqrt(70.0)))/900.0, (322.0-13.0*(np.sqrt(70.0)))/900.0]
Node_r = [0,r2,r3,r4,r5]
Weight_c = [0,c2,c3,c4,c5]

def Solver(function, points, limit):
    """
    Solves the integral
    """
    #Please insert formula in lambda function
    #######################################
    if function == "eg1":
        fx = lambda x,w: w*(x)
#    elif
    #######################################
    
    xi,wi = extract_XiWi(points, limit)
    Solution = 0.0
    for x, w in zip(xi, wi):
        Solution += fx(x,w)
    return Solution

def extract_XiWi(points, limit):
    """
    Extracts the proper nodes and weights to the required limits
    """
    N_r,W_c = Node_r[points-1], Weight_c[points-1]
    [a,b] = limit
    F_xi = lambda a,b,r: r*((b-a)/2) + (a+b)/2
    F_wi = lambda a,b,c: ((b-a)/2)*c
    xi = [F_xi(a,b,r) for r in N_r]
    wi = [F_wi(a,b,c) for c in W_c]
    return xi, wi

