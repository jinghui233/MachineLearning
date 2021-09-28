import matplotlib.pyplot as plt
import numpy as np
from GraphicDisplay import GraphicDisplay as Player


class LogisticRegression:
    def __init__(self):
        self.player = Player()
        self.player.register_key_event(self.on_button_press)
        self.class1 = []
        self.class2 = []
        self.curclass = self.class1

    def generateData(self):
        self.player.addPointsShow([1, 100], [1, 100])
        self.player.show()

    def on_button_press(self, event):
        if event.key == "left":
            self.curclass = self.class1
        elif event.key == "right":
            self.curclass = self.class2
        if event.key is None:
            self.curclass.append([event.xdata, event.ydata])
            self.update()

    def update(self):
        self.player.clear()
        if len(self.class1) > 0:
            npc1 = np.array(self.class1)
            self.player.addPointsShow(npc1[:, 0], npc1[:, 1],"red")
        if len(self.class2) > 0:
            npc2 = np.array(self.class2)
            self.player.addPointsShow(npc2[:, 0], npc2[:, 1], "green")

    def getTrainData(self):
        pass


if __name__ == "__main__":
    lr = LogisticRegression()
    lr.generateData()
