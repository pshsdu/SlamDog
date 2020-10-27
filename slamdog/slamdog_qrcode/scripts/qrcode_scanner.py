#!/usr/bin/env python

from __future__ import print_function

<<<<<<< HEAD
import os

=======
>>>>>>> 608848bc16aceef6317965998409063c282f5d82
from std_msgs.msg import Int32

import rospy
import cv2
import qrcode_data_server
<<<<<<< HEAD
import stack
=======
>>>>>>> 608848bc16aceef6317965998409063c282f5d82
from nav_msgs.msg import Odometry
import pyzbar.pyzbar as pyzbar
from pyasn1.compat.octets import null
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
<<<<<<< HEAD
from std_msgs.msg import String
=======
>>>>>>> 608848bc16aceef6317965998409063c282f5d82


class QRcodeScanner:
    scanned_data = []
    destination_odem = [[null for col in range(6)] for row in range(10)]

<<<<<<< HEAD
    index_stack = stack.Stack()
    odom_stack = stack.Stack()

    scanned_data_index = 0
    is_saved = False
    flag = False

    file_loc = "/catkin_ws/src/slamdog/slamdog_qrcode/data/qr_code_data.txt"
=======
    scanned_data_index = 0
>>>>>>> 608848bc16aceef6317965998409063c282f5d82

    def __init__(self):

        rospy.loginfo("start!")
<<<<<<< HEAD
        loc_list = (os.getcwd().split(os.path.sep))
        QRcodeScanner.file_loc = "/home/" + loc_list[2] + QRcodeScanner.file_loc

        self.bridge = CvBridge()
        self.image_received = False
        self.pub = rospy.Publisher('qrcode_scan', String, queue_size=3)

        # Connect image topic
        # /raspicam_node/image
=======

        self.bridge = CvBridge()
        self.image_received = False

        # Connect image topic
>>>>>>> 608848bc16aceef6317965998409063c282f5d82
        img_topic = "/camera/rgb/image_raw"
        rospy.Subscriber(img_topic, Image, self.callback)

        save_topic = "/ros_tutorial_msg"
        rospy.Subscriber(save_topic, Int32, self.write_file)

        while not rospy.is_shutdown():
            self.callback
            self.write_file

    def callback(self, data):
        # print(is_btn_clicked)
        # Convert image to OpenCV format
<<<<<<< HEAD

=======
>>>>>>> 608848bc16aceef6317965998409063c282f5d82
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        except CvBridgeError as e:
            print(e)

        self.image_received = True
        self.image = cv_image

        self.qrcode_decode(cv_image)

    def write_file(self, data):
<<<<<<< HEAD

        if not QRcodeScanner.is_saved:
            f = open(QRcodeScanner.file_loc, 'w')

            while not QRcodeScanner.index_stack.is_empty():
                data = "%" + str(QRcodeScanner.index_stack.pop()) + "\n"
                f.write(data)

                data_odom = QRcodeScanner.odom_stack.pop()
                # print(data_odom[0])
                for i in range(0, 6):
                    data = str(data_odom[i]) + "\n"
                    f.write(data)

            print("----------file saved----------")
            print("location : " + QRcodeScanner.file_loc)
            QRcodeScanner.is_saved = True
            f.close()

    def qrcode_decode(self, img):

        # if self.scanned_data_index == 0:
        #     rospy.Subscriber('odom', Odometry, self.get_odom)
=======
        print(data)

        output1 = QRcodeScanner.scanned_data
        output2 = QRcodeScanner.destination_odem

        f = open("/home/daeun/catkin_ws/src/slamdog/slamdog_qrcode/data/qr_code_data.txt", 'w')

        for i in range(0, len(output1)):
            data = "%" + str(output1[len(output1)-i-1]) + "\n"
            f.write(data)

            for j in range(0, 6):
                data = str(output2[i][j]) + "\n"
                f.write(data)

        print("file saved!")
        f.close()

    def qrcode_decode(self, img):

        if self.scanned_data_index == 0:
            rospy.Subscriber('odom', Odometry, self.get_odom)
>>>>>>> 608848bc16aceef6317965998409063c282f5d82

        if self.image_received:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded = pyzbar.decode(gray)

            for d in decoded:

                barcode_data = d.data.decode("utf-8")
                text = barcode_data

<<<<<<< HEAD
                # QRcodeScanner.scanned_data.append(text)
                # QRcodeScanner.scanned_data = list(set(QRcodeScanner.scanned_data))

                if QRcodeScanner.index_stack.is_empty() | (QRcodeScanner.index_stack.peek() != text):
                    QRcodeScanner.index_stack.push(text)
                    QRcodeScanner.flag = True
                    print("-----------------------------------")
                    print(QRcodeScanner.index_stack.peek())
                    rospy.Subscriber('odom', Odometry, self.get_odom)

                    for i in range(0, 5):
                        self.pub.publish(text)

                # if self.scanned_data_index != len(QRcodeScanner.scanned_data):
                #
                #     self.print_in_list()
                #     self.scanned_data_index += 1
=======
                QRcodeScanner.scanned_data.append(text)
                QRcodeScanner.scanned_data = list(set(QRcodeScanner.scanned_data))

                if self.scanned_data_index != len(QRcodeScanner.scanned_data):
                    rospy.Subscriber('odom', Odometry, self.get_odom)
                    self.print_in_list()
                    self.scanned_data_index += 1
>>>>>>> 608848bc16aceef6317965998409063c282f5d82

    def get_odom(self, msg):

        try:
            pos_x = msg.pose.pose.position.x
            pos_y = msg.pose.pose.position.y

            quat_x = msg.pose.pose.orientation.x
            quat_y = msg.pose.pose.orientation.y
            quat_z = msg.pose.pose.orientation.z
            quat_w = msg.pose.pose.orientation.w

<<<<<<< HEAD
            odom_list = [round(pos_x, 2), round(pos_y, 2), round(quat_x, 2), round(quat_y, 2), round(quat_z, 2), round(quat_w, 2)]

            # if QRcodeScanner.odom_stack.is_empty():
            #     QRcodeScanner.odom_stack.push(odom_list)
            #     print(QRcodeScanner.odom_stack.peek())
            # elif QRcodeScanner.odom_stack.peek() != odom_list:
            #     QRcodeScanner.odom_stack.push(odom_list)
            #     print(QRcodeScanner.odom_stack.peek())

            if QRcodeScanner.flag:
                QRcodeScanner.odom_stack.push(odom_list)
                print(QRcodeScanner.odom_stack.peek())
                QRcodeScanner.flag = False
=======
            QRcodeScanner.destination_odem[self.scanned_data_index][0] = round(pos_x, 2)
            QRcodeScanner.destination_odem[self.scanned_data_index][1] = round(pos_y, 2)
            QRcodeScanner.destination_odem[self.scanned_data_index][2] = round(quat_x, 2)
            QRcodeScanner.destination_odem[self.scanned_data_index][3] = round(quat_y, 2)
            QRcodeScanner.destination_odem[self.scanned_data_index][4] = round(quat_z, 2)
            QRcodeScanner.destination_odem[self.scanned_data_index][5] = round(quat_w, 2)
>>>>>>> 608848bc16aceef6317965998409063c282f5d82

        except():
            pass

<<<<<<< HEAD
=======
    def print_in_list(self):

        print("index : ", self.scanned_data_index)

        for i in range(0, len(QRcodeScanner.scanned_data)):
            if QRcodeScanner.scanned_data is not None:
                print(QRcodeScanner.scanned_data[i], end="  ")

        print()

        for i in range(0, len(QRcodeScanner.destination_odem)):
            if QRcodeScanner.destination_odem is not None:
                print(QRcodeScanner.destination_odem[i], end=" ")

        print()

>>>>>>> 608848bc16aceef6317965998409063c282f5d82

if __name__ == '__main__':

    rospy.init_node('qrcode_scanner', anonymous=True)
    scanner = QRcodeScanner()
