import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import nltk
import os

nltk.download('punkt')

class Plots:
    # by default a bar graph of token counts
    def __init__(self):
        self.message = ""
        self.type = "bar"
        self.analyze = False
        self.distribution = []
        self.sets = []
        self.opts = ["bar", "density"]

    def create_dist(self):
        unique = set(self.message)
        self.sets = list(unique)
        chars = list(self.message)
        for char in unique:
            self.distribution.append(chars.count(char))

    def draw(self, message, types=None, show = False):
        if message == "":
            raise Exception("Enter a message to get a graph")
        self.message = message
        if types in self.opts:
            self.type = types
        self.create_dist()

        if self.type == "bar":
            plt.bar(range(len(self.distribution)), self.distribution, color="r")
            plt.xticks(range(len(self.distribution)), self.sets)
            if show:
                plt.show()

        if self.type == "density":
            density = gaussian_kde(self.distribution)
            xs = np.linspace(0, len(self.distribution), 400)
            density.covariance_factor = lambda: 0.25
            density._compute_covariance()
            plt.title("Density plot for your message")
            plt.plot(xs, density(xs))
            if show:
                plt.show()
            else:
                return xs

    def analysis(self, analyze=True, show=False):
        self.analyze = analyze
        if self.message == "":
            raise Exception("Plot a graph first with using draw() function")
        if self.analyze:
            words = nltk.word_tokenize(self.message)
            f = nltk.probability.FreqDist(word.lower() for word in words).values()
            plt.bar(range(len(f)),f,color='b')
            plt.xticks(range(len(f)),list(set(words)),rotation=90)
            if show:
                plt.show()
            else:
                return f

    def analyze_with_file(self, file: str, return_words = False, return_freq = True):
        if file == "":
            raise Exception("We need a filename")
        if not os.path.exists(file):
            raise Exception("File does not exist in the same directory")
        f = open(file)
        wrds = nltk.sent_tokenize(f.read())
        f.close()
        if return_words:
            return wrds
        freq = nltk.FreqDist(words.lower() for words in wrds).values()
        if return_freq:
            return freq
