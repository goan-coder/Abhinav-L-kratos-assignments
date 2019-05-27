#!/usr/bin/env python

import sys
import rospy
from assignment1.srv import *
b=True
def task2_client(x, y, z):
    rospy.wait_for_service('task2')
    try:
        task_2 = rospy.ServiceProxy('task2', task2)
        resp1 = task_2(x, y, z)
        return resp1.d
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        b=False
def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "%s"%(task2_client(x, y, z))
    if b==True:
	print "True"
    else:
	print "False"
