import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

class Plots:
    # by default a bar graph of token counts
    def __init__(self):
        self.message = ""
        self.type = "bar"
        self.analyze = False
        self.distribution = []
        self.sets = []

    def create_dist(self):
        unique = set(self.message)
        self.sets = list(unique)
        chars = list(self.message)
        for char in unique:
            self.distribution.append(chars.count(char))


    def draw(self,message,type = None):
        self.message = message
        if type is not None:
            self.type = type
        self.create_dist()
        if self.type == "bar":
            plt.bar(range(len(self.distribution)), self.distribution,color='r')
            plt.xticks(range(len(self.distribution)),self.sets)
            plt.show()
        if self.type == "density":
            density = gaussian_kde(self.distribution)
            xs = np.linspace(0,len(self.distribution), 400)
            density.covariance_factor = lambda : .25
            density._compute_covariance()
            plt.title("Density plot for your message")
            plt.plot(xs, density(xs))
            plt.show()