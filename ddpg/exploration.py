import numpy as np

class ExplorationPolicy():
    
    def __init__(self, sigma):
        self.sigma = sigma

    def get_noise(self, action):
        return action + np.random.normal(0, self.sigma)

class OUPolicy(ExplorationPolicy):

    def __init__(self, mean, theta, sigma):
        self.mean = mean
        self.theta = theta
        self.sigma = sigma

    def get_noise(self, action):
        return action + self.theta * (self.mean - action) + np.random.normal(0, self.sigma)




