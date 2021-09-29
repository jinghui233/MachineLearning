import matplotlib.pyplot as plt
import numpy as np
from MainDir.GraphicDisplay.GraphicDisplay import GraphicDisplay as Player


class LogisticRegression:
    def __init__(self):
        self.player = Player()
        self.player.register_key_event(self.on_button_press)
        self.class1 = []
        self.class2 = []
        self.curclass = self.class1
        self.class1, self.class2 = self.load()

    def generateData(self):
        self.update()
        self.player.show()

    def on_button_press(self, event):
        if event.key == "left":
            self.curclass = self.class1
        elif event.key == "right":
            self.curclass = self.class2
        elif event.key == "enter":
            self.save()
        if event.key is None:
            self.curclass.append([event.xdata, event.ydata])
            self.update()

    @staticmethod
    def load():
        class1 = []
        class2 = []
        with open(f"D:\\ProjectCode\\LTest\\MachineLearning\\MainDir\\GraphicDisplay\\Debug\\LogisticRegression.txt", 'r') as f:
            strs = f.readlines()
        str0sp = strs[0].split(";")
        for str0 in str0sp:
            class1.append([float(str0.split(",")[0]), float(str0.split(",")[1])])
        str1sp = strs[1].split(";")
        for str1 in str1sp:
            class2.append([float(str1.split(",")[0]), float(str1.split(",")[1])])
        return class1, class2

    def save(self):
        savestr = []
        for p in self.class1:
            savestr.append(f"{p[0]},{p[1]}")
        c1str = ";".join(savestr)
        savestr = []
        for p in self.class2:
            savestr.append(f"{p[0]},{p[1]}")
        c2str = ";".join(savestr)
        print(c1str)
        with open(f"Debug\\LogisticRegression.txt", 'w') as f:
            f.write(f"{c1str}\n{c2str}")

    def update(self):
        self.player.clear()
        self.player.addPointsShow([1, 100], [1, 100], alpha=0)
        if len(self.class1) > 0:
            npc1 = np.array(self.class1)
            self.player.addPointsShow(npc1[:, 0], npc1[:, 1], "red")
        if len(self.class2) > 0:
            npc2 = np.array(self.class2)
            self.player.addPointsShow(npc2[:, 0], npc2[:, 1], "green")

    @staticmethod
    def classtonparray(class1, class2):
        classall = []
        for c1 in class1:
            classall.append([c1[0], c1[1], 0])
        for c2 in class2:
            classall.append([c2[0], c2[1], 1])
        return np.array(classall)

    @staticmethod
    def nparraytoclass(npm):
        class1 = []
        class2 = []
        for npmin in npm:
            if npmin[2] == 0:
                class1.append([npmin[0], npmin[1]])
            else:
                class2.append([npmin[0], npmin[1]])
        return class1, class2

    @staticmethod
    def getTrainData():
        class1, class2 = LogisticRegression.load()
        return LogisticRegression.classtonparray(class1, class2)


if __name__ == "__main__":
    lr = LogisticRegression()
    lr.generateData()
    # npm = lr.classtonparray(lr.class1, lr.class2)
    # lr.nparraytoclass(npm)
