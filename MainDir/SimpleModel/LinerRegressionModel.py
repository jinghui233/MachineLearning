from typing import List
from MainDir.GraphicDisplay.LinerRegressionDisplay import LinerRegressionDisplay

import numpy as np


class LinerRegressionModel:
    def __init__(self):
        self.player = LinerRegressionDisplay()
        n_samples = 30
        train_x = np.linspace(0, 20, n_samples)
        train_y = 3 * train_x * train_x + 4 * np.random.rand(n_samples)
        train_set = np.ndarray((len(train_x), 2))
        train_set[:, 0] = train_x
        train_set[:, 1] = train_y
        self.ratea = 0.00001
        self.theta = np.array([0, 0, 0])
        self.train_set = train_set
        self.player.register_key_event(self.on_click)
        self.player.show()

    def calc_d_theta(self, theta: np.array, train_set: np.array):
        dtheta = np.zeros(theta.shape)
        for index in range(len(train_set)):
            dtheta[0] += theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] ** 2 - train_set[index][1]
            dtheta[1] += (theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] ** 2 - train_set[index][1]) * train_set[index][0]
            dtheta[2] += (theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] ** 2 - train_set[index][1]) * train_set[index][0] ** 2
        dtheta /= len(train_set)
        return dtheta

    def on_click(self, event):
        self.train()

    def train(self):
        dtheta = self.calc_d_theta(self.theta, self.train_set)
        self.theta = self.theta - dtheta * self.ratea
        print(self.theta)
        self.player.clear()
        self.player.addEquationShow(self.train_set[:, 0], self.theta)
        self.player.addPointsShow(self.train_set[:, 0], self.train_set[:, 1])


if __name__ == "__main__":
    model = LinerRegressionModel()
    model.train()
