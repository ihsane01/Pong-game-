import game as g
import matplotlib.pylab as plt
import numpy as np

def plot_agent_reward(rewards):
    """ Function to plot agent's accumulated reward vs. iteration """
    plt.plot(np.cumsum(rewards))
    plt.title('Agent Cumulative Reward vs. Iteration')
    plt.ylabel('Reward')
    plt.xlabel('Episode')
    plt.show()

class GameLearning:

    def __init__(self):
        while True:
            print('\n*******  choisir le mode de jeu : ********')
            type = input('1- AgentRL vs AgentAI \n2- AgentRL vs Human \n3- AgentRL vs AgentRL\n le mode est = ')
            if type == '1' or type == '2' or type == '3':
                break
        if type == '1':
            self.game = g.Game('agentAI')
        elif type == '2':
            self.game = g.Game('human')
        else:
            self.game = g.Game('agentRL')

    def beginPlaying(self):
        self.game.play()

if __name__ == '__main__':
    gl = GameLearning()
    gl.beginPlaying()
