#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3

def scan_values(msg, pub):
#takes the data from the laser scanner.
	global mean_distance
	valid_range = []
	for i in range(5):
		if msg.ranges[i] > 0 and msg.ranges[i] < 8:
			valid_range.append(msg.range[i])
			print valid_range + "valid_range value"
		if len(valid_range) > 0:
			mean_distance = sum(valid_ranges)/float(len(valid_range))
			print mean_distance + "valid_range is > 0"
		else:
			mean_distance = -1.0

def follow():
	pub = rospy.Publisher ('cmd_vel',  Twist, queue_size=10)
	sub = rospy.Subscriber ('scan', LaserScan, scan_recieved, pub)
	rospy.init_node('teleop', anonymous = True)
	r = rospy.Rate(10) #10hz
	while not rospy.is_shutdown():
		if mean_distance != -1.0
			velocity_msg = Twist
	pub.publish(msg)
	r.sleep()

if __name__ == '__main__':
	try:
		teleop()
	except rospy.ROSInterruptException: pass