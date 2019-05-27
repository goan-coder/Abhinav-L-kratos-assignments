#!/usr/bin/env python

from assignment1.srv import *
import rospy

def handle_task_3(req):
    c=0
    b=rospy.get_time()
    while True:
	s=raw_input()
        c=c+1	
	if s==req.a:
		break
    d=rospy.get_time()
    e=d-b
    result="No of Feedback Entered %i Time elapsed %i secs" %(c,e)		
    return Task3Response(result)

def task_3_server():
    rospy.init_node('task_3_server')
    s = rospy.Service('task_3', Task3, handle_task_3)
    print "Ready."
    rospy.spin()

if __name__ == "__main__":
    task_3_server()
