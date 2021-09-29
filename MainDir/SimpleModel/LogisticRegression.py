import numpy as np


class LogisticRegression:
    def __init__(self):
        self.ratea = 0.1

    def calc_d_theta(self, theta: np.array, train_set: np.array):
        dtheta = np.zeros(theta.shape)
        for index in range(len(train_set)):
            dtheta[0] = theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] * train_set[index][0] - train_set[index][1]
            dtheta[1] = (theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] * train_set[index][0] - train_set[index][1]) * train_set[index][0]
            dtheta[2] = (theta[0] + theta[1] * train_set[index][0] + theta[2] * train_set[index][0] * train_set[index][0] - train_set[index][1]) * train_set[index][0] * \
                        train_set[index][0]
        dtheta /= len(train_set)
        return dtheta