#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan

#all the sensor measurement values and stores them
front_distance = 0
right_distance = 0
left_distance = 0

#scans for the distance away from the wall and stores the values for later use
def scanFront(msg, pub):
	x = 1
	while x>0:
		front_distance = msg.ranges[0]
		right_distance = msg.ranges[90]
		left_distance = msg.ranges[270]
		print "Front distance: " + msg.ranges[0]
		print "Right distance: " + msg.ranges[90]
		print "left distance: " + msg.ranges[270]

def follow_wall():
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('/scan', LaserScan, scanFront)
	rospy.init_node('follow_wall', anonymous=True)
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		if (front_distance == -1): #If it is a foot away from the wall
			if(left_distance != -1.0): #turn toward the left
				msg = Twist(Vector3(0.0, 0.0, 0.0), Vector3(0.2*(left_distance - 1.0), 0.0,0.0))
			else: #once it is turned to the right, it will move forward in a straight line forever
				msg = Twist(Vector3(1.0, 0.0, 0.0), Vector3(0.0, 0.0, 0.0))
		else: #if it is not a meter away from the wall
			msg = Twist(Vector3(0.0, 0.0, 0.2*(front_distance - 1.0)), Vector3(0.0, 0.0, 0.0))
		pub.publish(msg)
		r.sleep()


if __name__ == '__main__':
    try:
        follow_wall()
    except rospy.ROSInterruptException: pass