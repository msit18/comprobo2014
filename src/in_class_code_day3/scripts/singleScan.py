#!/usr/bin.env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

def 

if __name__ == '__main__':
  18     rospy.init_node('singleScan')
  19     reading = rospy.get_param('scan_recieved')
  20     rospy.Subscriber('/%s/pose' % singleScan,
  21                      turtlesim.msg.Pose,
  22                      handle_turtle_pose,
  23                      singleScan)
  24     rospy.spin()