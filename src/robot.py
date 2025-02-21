import numpy as np
import random

THETALIST = [0, np.pi/2, np.pi, 3/2*np.pi]

class Robot:

    SENSOR_NOISE_COEF = 0.1
    ANG_VEL_COEF = np.pi / 2
    LIN_VEL_COEF = 1
    VIEW_DIST = 5
    NUM_DISTS = 5
    THETALIST = [0, np.pi / 2, np.pi, 3 / 2 * np.pi]
    
    def __init__(self, init_pose, fov):
        self.pose = init_pose
        self.fov = fov

    
    def move(self, vel, map):
        curr_theta = THETALIST[self.pose[2]]

        new_x = self.pose[0] + vel[0] * np.cos(curr_theta) * self.LIN_VEL_COEF
        new_y = self.pose[1] + vel[0] * np.sin(curr_theta) * self.LIN_VEL_COEF
        new_or = (self.pose[2] + vel[1]) % 4
        new_theta = THETALIST[new_or]

        if vel[1] != 0:
            new_x = new_x + vel[0] * np.cos(new_theta) * self.LIN_VEL_COEF
            new_y = new_y + vel[0] * np.sin(new_theta) * self.LIN_VEL_COEF

        new_x = int(np.rint(new_x))
        new_y = int(np.rint(new_y))
        new_or = int(np.rint(new_or))

        if map.checkForObstacle(new_x, new_y):
            return self.pose
        else:
            self.pose = (new_x, new_y, new_or)
            return self.pose


    def senseRobot(self, other_pose):
        dist = np.sqrt(np.square(self.pose[0]-other_pose[0]) + np.square(self.pose[1]-other_pose[1]))
        ang =  np.arctan2(other_pose[1]-self.pose[1], other_pose[0]-self.pose[0])

        if np.abs(ang - self.pose[2]) > self.fov/2:
            return 1

        reading = np.round((dist + dist * random.gauss(0,1) * self.SENSOR_NOISE_COEF)/(self.VIEW_DIST/self.NUM_DISTS))
        if reading < 0:
            reading = 0
        if reading > self.NUM_DISTS:
            reading = self.NUM_DISTS+1

        if reading < self.NUM_DISTS+1:
            return 0
        else:
            return 1


