import gym
from baseAgentFile import BaseAgent

# The gym environment
env = gym.make('CartPole-v0')

# We recreate your agent and load it
agent = BaseAgent()
agent.load("best_param_200.npy")

# This is the testing loop, try and get a high score!
score = 0
nr_games = 100
for _ in range(nr_games):
    state = env.reset()
    done = False
    while not done:
        action = agent.action(state)
        state, reward, done, info = env.step(action)
        score += reward
avg_score = score / nr_games

print("Final score:", avg_score)
