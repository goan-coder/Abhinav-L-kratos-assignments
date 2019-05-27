#!/usr/bin/env python

import sys
import rospy
from assignment1.srv import *

def task_3_client(x):
    rospy.wait_for_service('task_3')
    try:
        task_3 = rospy.ServiceProxy('task_3', Task3)
        resp1 = task_3(x)
        return resp1.c
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "%s"%(task_3_client(x))
