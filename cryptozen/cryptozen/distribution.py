import matplotlib.pyplot as plt

class Plots:
    # by default a bar graph of token counts
    def __init__(self):
        self.message = ""
        self.type = "bar"
        self.analyze = False
        self.distribution = []

    def draw(self,message,type = None):
        self.message = message
        if type is not None:
            self.type = type
        if self.type == "bar":
            unique = set(message)
            chars = list(message)
            for char in unique:
                self.distribution.append(chars.count(char))

            plt.bar(range(len(self.distribution)), self.distribution,color='r')
            plt.xticks(range(len(self.distribution)),list(unique))
            plt.show()