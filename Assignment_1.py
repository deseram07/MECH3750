import numpy as np
import sys
import Gaussian_Quadrature_Solver as G_Solver



def main(section):#,function, bounds, no_points):
#    limit_str = bounds.split(',')
#    limit = [float(item) for item in limit_str]
#    points = int(no_points)
    
#    if len(limit) != 2:
#        print "Error: Two bounds are required!!"
#        sys.exit(1)
#    if points < 1 or points > 5:
#        print "Error: Number of points are required to be between 2 and 5"
#        sys.exit(2)
#    
    if int(section) == 1:
        """
        Solves known function
        """
        s_points = [2,5]
        s_limit = [0.0, 1.0]
        for point in s_points:
            print "Solution from using " + str(point) + " point Quadrature for [f'(x) = x]:" + str(G_Solver.Solver("eg1", point, s_limit))        
#    elif section == 3:
        
        
    
if __name__ == '__main__':
    if(len(sys.argv) is not 2):
        print "Usage: python Assignment_1.py [Assignment part: 1 or 3] [Function: 1, 2, 3 or 4] [bounds: start,stop] [no points]"
        sys.exit(1)
    else:
        main(sys.argv[1]) #, sys.argv[2], sys.argv[3], sys.argv[4])