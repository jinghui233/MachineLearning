import matplotlib.pyplot as plt
import numpy as np
import time


class GraphicDisplay:
    def __init__(self):
        self.stop = False
        self.func = None
        fig, ax = plt.subplots()

        fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        fig.canvas.mpl_connect('button_press_event', self.on_key_press)

    def on_key_press(self, event):
        print(f"{event.xdata}:{event.ydata}-{event.key}")
        if __name__ == "__main__":
            self.stop = True
        if self.func is not None:
            self.func(event)

    def register_key_event(self, func):
        self.func = func

    def addlineShow(self, x, y):
        plt.plot([1, 100], [1, 100], alpha=0)
        plt.plot(x, y)

    def addPointsShow(self, x, y, color="coral"):
        plt.plot([1, 100], [1, 100], alpha=0)
        plt.plot(x, y, 'o', color=color)

    def clear(self):
        plt.cla()

    def update(self):
        pass

    def show(self):
        self.stop = False
        while not self.stop:
            plt.pause(0.01)


def test(event):
    print(event)


if __name__ == "__main__":
    player = GraphicDisplay()
    player.register_key_event(test)
    x = np.arange(0, 10, 1)
    player.addPointsShow(x, x + 1)
    player.show()
    player.clear()
    player.addlineShow(x, x + 1)
    player.show()
