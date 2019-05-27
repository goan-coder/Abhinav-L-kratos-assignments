#!/usr/bin/env python

from assignment1.srv import *
import rospy

def handle_task2(req):
	if req.c==1:
    		return task2Response(req.a + req.b)
	elif req.c==2:
		return task2Response(req.a - req.b)
	elif req.c==3:
		return task2Response(req.a * req.b)
	elif req.c==4:
		return task2Response(req.a / req.b)
        else:
		return 0

def server_task2():
    rospy.init_node('server_task2')
    s = rospy.Service('task2', task2, handle_task2)
    print "Ready."
    rospy.spin()

if __name__ == "__main__":
    server_task2()
