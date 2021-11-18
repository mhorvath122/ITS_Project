#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from multiprocessing import Process, Value



def callback(data):

    #Robot controll logic:

    print(data.data)
    if data.data == 'Stop':
        linear_x.value = 0.0;
        linear_y.value = 0.0; 
        angular_z.value = 0.0;

    elif data.data == 'Turn right ahead':
        linear_x.value = 0.5;
        linear_y.value = 0.0; 
        angular_z.value = 0.3;

    elif data.data == 'Turn left ahead':
        linear_x.value = 0.5;
        linear_y.value = 0.0; 
        angular_z.value = -0.3;

    elif data.data == 'Ahead only':
        linear_x.value = 0.5;
        linear_y.value = 0.0; 
        angular_z.value = 0.0;

    elif data.data == 'Keep right':
        linear_x.value = 0.0;
        linear_y.value = 0.5; 
        angular_z.value = 0.0;

    elif data.data == 'Keep left':
        linear_x.value = 0.0;
        linear_y.value = -0.5; 
        angular_z.value = 0.0;

    else:
        pass





def talker(x,y,z):

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('robot_control_logic', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist.linear.x = linear_x.value;
        twist.linear.y = linear_y.value; twist.linear.z = 0;
        twist.angular.x = 0; twist.angular.y = 0;
        twist.angular.z = angular_z.value;
        pub.publish(twist)
        rate.sleep()

def listener(x,y,z):

    rospy.init_node('prediction_listener', anonymous=True)
    rospy.Subscriber("prediction", String, callback)
    rospy.spin()



if __name__ == '__main__':

    twist = Twist()
    
    linear_x = Value('d',0.0)
    linear_y = Value('d',0.0)
    angular_z = Value('d',0.0)

    t = Process(target=talker, args = [linear_x, linear_y, angular_z,])
    l = Process(target=listener, args = [linear_x, linear_y, angular_z,])
    t.start()
    l.start()
    t.join()
    l.join()

