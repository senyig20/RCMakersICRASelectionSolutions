#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
int frontSensor = 0
int leftSensor = 0
int rightSensor = 0

def scan0(data):
    frontSensor = data.data
def scan1(data):
    leftSensor = data.data
def scan2(data):
    rightSensor = data.data


//edit heredef convert():
    rospy.init_node('MazeSolver')
    initSubs()
    pub=rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(dataArray)
        rate.sleep()

def initSubs():
    rospy.Subscriber("base_scan_0", LaserScan, scan0)
    rospy.Subscriber("base_scan_1", LaserScan, scan1)
    rospy.Subscriber("base_scan_2", LaserScan, scan2)



if __name__ == '__main__':
    try:
        convert()
    except rospy.ROSInterruptException:
        pass
