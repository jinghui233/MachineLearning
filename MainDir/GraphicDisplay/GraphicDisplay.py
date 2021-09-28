import matplotlib.pyplot as plt
import numpy as np
import cv2


class GraphicDisplay:
    def __init__(self):
        self.stop = False
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', self.on_key_press)

    def on_key_press(self, event):
        print(event.key)
        self.stop = True

    def addEquationShow(self, x, theta):
        y = theta[0] + theta[1] * x + theta[2] * x * x
        plt.plot(x, y)

    def addlineShow(self, x, y):
        plt.plot(x, y)

    def addPointsShow(self, x, y):
        plt.plot(x, y, 'o')

    def clear(self):
        plt.cla()

    def show(self):
        self.stop = False
        while not self.stop:
            plt.pause(1)


if __name__ == "__main__":
    player = GraphicDisplay()
    x = np.arange(0, 10, 1)
    player.addEquationShow(x, [1, 0])
    player.show()
    player.addEquationShow(x, [1, 1])
    player.show()
