#!/usr/bin/env python

import rospy
import math
import numpy
from std_msgs.msg import Float64MultiArray, Int64MultiArray
from ass12.msg import AngleWithStats
dataArray = []

def arr0(data):
    dataArray[0] = math.radians(data.data)
def arr1(data):
    dataArray[1] = math.radians(data.data)
def arr2(data):
    dataArray[2] = math.radians(data.data)
def arr3(data):
    dataArray[3] = math.radians(data.data)
def arr4(data):
    dataArray[4] = math.radians(data.data)
def arr5(data):
    dataArray[5] = math.radians(data.data)



def AngleStats():
    rospy.init_node('converter', anonymous=True)
    initSubs()
    pub=rospy.Publisher('/standing2/joint_impedance_controller/position', Float64MultiArray, queue_size=10)
    rate=rospy.Rate(10)
    msg = AnglesWithStats()
    while not rospy.is_shutdown():
        msg.Angles = dataArray
        msg.Mean = numpy.mean(dataArray)
        msg.Median = numpy.median(dataArray)
        pub.publish(msg)
        rate.sleep()

def initSubs():
    rospy.Subscriber("/standing2middleMan/J1Angle", Int64, arr0)
    rospy.Subscriber("/standing2middleMan/J2Angle", Int64, arr1)
    rospy.Subscriber("/standing2middleMan/J3Angle", Int64, arr2)
    rospy.Subscriber("/standing2middleMan/J4Angle", Int64, arr3)
    rospy.Subscriber("/standing2middleMan/J5Angle", Int64, arr4)
    rospy.Subscriber("/standing2middleMan/J6Angle", Int64, arr5)



if __name__ == '__main__':
    try:
        convert()
    except rospy.ROSInterruptException:
        pass
