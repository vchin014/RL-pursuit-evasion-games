import numpy as np
from robot import Robot

class Map:

    grid_sz = (20, 20)
    fov = np.pi

    def __init__(self):
        self.grid = np.zeros(self.grid_sz)
        for i in range(self.grid_sz[0]//10):
            for j in range(self.grid_sz[1]//10):
                self.grid[(i*10):(i*10)+5, (j*10):(j*10)+5] = np.ones((5,5))

        self.r_p = Robot((0,0,0), self.fov)
        self.r_e = Robot((0,0,0), self.fov)


    def pursuerScanner(self):
        return self.r_p.senseRobot(self.r_e.pose)

    def evaderScanner(self):
        return self.r_e.senseRobot(self.r_p.pose)

    def haveCollided(self):
        dist = np.sqrt(np.square(self.r_p.pose[0]-self.r_e.pose[0]) + np.square(self.r_p.pose[1]-self.r_e.pose[1]))
        if dist <= 1.5:
            return True
        else:
            return False

    def checkForObstacle(self, x, y):
        x = int(x)
        y = int(y)

        if y > self.grid.shape[0] - 1 or y < 0 or x > self.grid.shape[0] - 1 or x < 0:
            return True
        elif self.grid[x, y] == 1:
            return True
        else:
            return False
