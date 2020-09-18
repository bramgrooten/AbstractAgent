from abstractAgentFile import AbstractAgent
import numpy as np


class BaseAgent(AbstractAgent):
    def __init__(self, *args, **kwargs):
        self.param = np.random.rand(4)
        self.best_score = 0
        self.best_param = np.random.rand(4)

    def __str__(self):
        return f"BaseAgent (param={self.param}, best_param={self.best_param}, best_score={self.best_score})"

    def __repr__(self):
        return f"<{self.__class__.__name__} (param={self.param})>"

    def train(self, score):
        if score > self.best_score:
            self.best_score = score
            self.best_param = self.param
        else:
            self.param = np.random.rand(4)

    def action(self, obs):
        return 0 if np.sum(np.multiply(self.param, obs)) < 0 else 1


    def load(self, params = "best_param.npy"):
        with open(params, "rb") as file:
            self.param = np.load(file)

    def save(self):
        with open("best_param.npy", "wb") as file:
            np.save(file, self.param)




