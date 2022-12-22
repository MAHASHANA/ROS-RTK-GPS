#!/usr/bin/env python
#-*- coding: utf-8 -*-
from gps_puck.msg import gps_msg
import serial
import rospy
import utm
from std_msgs.msg import String
import sys

rospy.init_node('mynode')
port = rospy.get_param("~port_number")

ser = serial.Serial(port=port, baudrate=57600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
pub = rospy.Publisher('gps', gps_msg, queue_size=10)

rate = rospy.Rate(10) # 10hz
msg = gps_msg()


while True: 
    sac = str(ser.readline())
    if 'GGA' in str(sac):
        print(sac)
        H = float(sac.split(",")[1])
        x = float(sac.split(",")[2])
        a = float(sac.split(",")[4])
        
        lat = str(x)
        lon = str(a)
        time = str(H)
        #print (float(lat[:2])+float(lat[2:])/60)
        sec = float(time[:2])*60*60+float(time[2:4])*60+float(time[4:6])
        nsec = (float(time[6:]))*10e6
        y = float(lat[:2])+float(lat[2:])/60
        z = (float(lon[:2])+float(lon[2:])/60)*-1
        gap = utm.from_latlon(float(y), float(z))
        msg.latitude = y
        msg.longitude = z
        msg.UTM_northing = gap[0]
        msg.UTM_easting = gap[1]
        msg.altitude = float(sac.split(",")[8])
        msg.Zone = gap[2]
        msg.FIX = int(sac.split(",")[6])
        msg.letter = gap[3]
        msg.Header.stamp.secs = int(sec)
        msg.Header.stamp.nsecs = int(nsec)
        msg.Header.frame_id = "GPS1_Frame"
        print(sec, nsec)
        print(f"lat long zone {gap}")

        pub.publish(msg)




