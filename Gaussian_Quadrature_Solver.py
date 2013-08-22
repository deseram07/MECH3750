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

def Solver(xi,wi):
    """
    Solves the integral
    """
    #Please insert formula in lambda function
    #######################################
    fx = lambda x,w: w*(x)
    #######################################
    
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

def main(Function, bounds, no_points):
    limit_str = bounds.split(',')
    limit = [float(item) for item in limit_str]
    points = int(no_points)
    
    if len(limit) != 2:
        print "Error: Two bounds are required!!"
        sys.exit(1)
    if points < 1 or points > 5:
        print "Error: Number of points are required to be between 2 and 5"
        sys.exit(2) 
    xi,wi = extract_XiWi(points, limit)
    print Solver(xi,wi)
    
if __name__ == '__main__':
    if(len(sys.argv) is not 4):
        print "Usage: python assignment1.py [Function] [bounds] [no points]"
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])