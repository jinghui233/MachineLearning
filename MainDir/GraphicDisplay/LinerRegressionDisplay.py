import matplotlib.pyplot as plt
import numpy as np
from MainDir.GraphicDisplay.GraphicDisplay import GraphicDisplay

class LinerRegressionDisplay(GraphicDisplay):
    def addEquationShow(self, x, theta):
        y = theta[0] + theta[1] * x + theta[2] * x * x
        plt.plot(x, y)



if __name__ == "__main__":
    player = LinerRegressionDisplay()
    x = np.arange(0, 10, 1)
    player.addEquationShow(x, [1, 0,1])
    player.show()
    player.clear()
    player.addEquationShow(x, [1, 1,1])
    player.show()
