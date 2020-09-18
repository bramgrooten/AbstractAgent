import gym

# Here we need to import your agent
from baseAgentFile import BaseAgent

agent = BaseAgent()

# The gym environment
env = gym.make('CartPole-v0')

# The training loop
for _ in range(10_000):
    state = env.reset()
    done = False
    score = 0
    while not done:
        # Here your agent needs to return an action
        action = agent.action(state)
        state, reward, done, info = env.step(action)
        score += reward

    # This is where you can train your agent given the score
    agent.train(score)
    print("Best score so far: {}".format(agent.best_score), end='\r')

# Now we are testing your loading and saving
agent.save()

# We remove the object just to be sure
del agent

# We recreate your agent and load it
agent = BaseAgent()
agent.load()

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


