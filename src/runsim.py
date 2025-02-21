import numpy as np
import matplotlib.pyplot as plt
import gym
from map import Map
from robot import Robot
from qlearning import TurtleBotTag

def main():
    # Loading Environment and Q-table structure
    env = TurtleBotTag()
    Q_p = np.zeros(env.Q_dim)
    Q_e = np.zeros(env.Q_dim)

    # Parameters of Q-learning
    eta = .005
    gma = .9
    epsilon = 1.1
    step_num = 999
    epis = 200000
    rev_list_p = []  # rewards per episode for pursuer
    rev_list_e = []  # rewards per episode for evader
    steps_list = []  # steps per episode
    env.RENDER_FREQ = 500000  # Rendering frequency
    env.RENDER_PLOTS = True  # Render plots
    # env.SAVE_PLOTS = False  # Save plots

    # 3. Training using Q-learning Algorithm
    for episode in range(epis):
    # Resetting environment
        state_p, state_e = env.reset()
        total_reward_p = 0
        total_reward_e = 0
        done = False
        step_count = 0
        
        if episode != 0:
            epsilon = 1 / np.floor(episode / epis / 20)
            
        env.epis = episode
        
        # Q-Table learning algorithm
        while step_count < step_num:
            env.step_num = step_count
            env.render()
            step_count += 1
            
            # Choosing action from Q table based on epsilon-greedy
            if np.random.rand() > epsilon:
                action_p = np.argmax(Q_p[state_p])
                action_e = np.argmax(Q_e[state_e])
            else:
                action_p = np.random.randint(0, env.action_space.n)
                action_e = np.random.randint(0, env.action_space.n)
            
            # Getting new state & reward from environment
            next_state_p, next_state_e, reward_p, reward_e, done = env.step(action_p, action_e)     
            
            # Update Q-Table with new knowledge
            Q_p[state_p][action_p] += eta * (reward_p + gma * np.max(Q_p[next_state_p]) - Q_p[state_p][action_p])
            Q_e[state_e][action_e] += eta * (reward_e + gma * np.max(Q_e[next_state_e]) - Q_e[state_e][action_e])
            
            total_reward_p += reward_p
            total_reward_e += reward_e
            state_p = next_state_p
            state_e = next_state_e
            
            if done:
                break
        
        rev_list_p.append(total_reward_p)
        rev_list_e.append(total_reward_e)
        steps_list.append(step_count)
        env.render()


    print("Pursuer Reward Sum on all episodes " + str(sum(rev_list_p)/epis))
    print("Evader Reward Sum on all episodes " + str(sum(rev_list_e)/epis))


if __name__ == '__main__':
    main()
