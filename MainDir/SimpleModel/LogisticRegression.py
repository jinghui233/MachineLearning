import numpy as np
from MainDir.GraphicDisplay.DataPrepare import LogisticRegression as LRData
from MainDir.GraphicDisplay.GraphicDisplay import GraphicDisplay


class LogisticRegression:
    def __init__(self):
        self.player = GraphicDisplay()
        self.ratea = 0.0001
        self.theta = np.array([0, 0])
        self.train_set = LRData.getTrainData()
        self.player.register_key_event(self.on_click)
        self.player.show()

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def calc_d_theta(self, theta: np.array, train_set: np.array):
        dtheta = np.zeros(theta.shape)
        for i in range(len(train_set)):
            dtheta[0] += (self.sigmoid(np.dot(theta, train_set[i, 0:2])) - train_set[i][2]) * train_set[i][0]
            dtheta[1] += (self.sigmoid(np.dot(theta, train_set[i, 0:2])) - train_set[i][2]) * train_set[i][1]
        dtheta /= len(train_set)
        return dtheta

    # -0.04840686647735886
    def on_click(self, event):
        self.train()

    def show(self, class1, class2):
        self.player.clear()
        self.player.addPointsShow([1, 100], [1, 100], alpha=0)
        if len(class1) > 0:
            npc1 = np.array(class1)
            self.player.addPointsShow(npc1[:, 0], npc1[:, 1], "red")
        if len(class2) > 0:
            npc2 = np.array(class2)
            self.player.addPointsShow(npc2[:, 0], npc2[:, 1], "green")

    def train(self):
        dtheta = self.calc_d_theta(self.theta, self.train_set)
        self.theta = self.theta - dtheta * self.ratea
        newset = np.ndarray(self.train_set.shape)
        newset[:, 0:2] = self.train_set[:, 0:2]
        for newsett in newset:
            if self.sigmoid(self.theta[0] * newsett[0] + self.theta[1] * newsett[1]) >= 0.5:
                newsett[2] = 1
            else:
                newsett[2] = 0
        class1, class2 = LRData.nparraytoclass(newset)
        self.show(class1, class2)


if __name__ == "__main__":
    model = LogisticRegression()
    # model.train()
