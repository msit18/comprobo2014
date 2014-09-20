#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan

mean_distance = -1.0
sub_distance = -1.0

#Processes data from the laser scanner, msg is of type sensor_msgs/LaserScan
def scanFront(msg, pub):
    global mean_distance
    valid_ranges = []
    for i in range(5):
        if (msg.ranges[i] > 0 and msg.ranges[i] < 45) and (msg.ranges[i] > 315 and msg.ranges[i] < 359):
            valid_ranges.append(msg.ranges[i])
    if len(valid_ranges) > 0:
        mean_distance = sum(valid_ranges)/float(len(valid_ranges))
    else:
        mean_distance = -1.0

def follow_wall():
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('/scan', LaserScan, scanFront)
	rospy.init_node('follow_wall', anonymous=True)
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		if (mean_distance != -1): #If it not a meter away from its targetted object
			msg = Twist(Vector3(0.2, 0.0, 0.0), Vector3(0.0, 0.0, 0.0))
		else: #if is a meter away from its targetted object
			msg = Twist(Vector3(0.0, 0.0, 0.0), Vector3(0.0, 0.0, 0.0))
		pub.publish(msg)
		r.sleep()


if __name__ == '__main__':
    try:
        follow_wall()
    except rospy.ROSInterruptException: pass