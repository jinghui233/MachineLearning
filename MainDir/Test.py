import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
epochs = 200

n_samples = 3
train_x = np.linspace(0, 20, n_samples)
train_y = 3 * train_x + 4 * np.random.rand(n_samples)
print(train_x)
print(train_x*train_x)
