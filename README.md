# 🏃‍♂️ Reinforcement Learning in Pursuit Evasion Games

## **Overview**
This project simulates a **game of tag** between two robots in a grid environment using the **Q-learning algorithm**.  
- **Pursuer:** Tries to catch the evader.  
- **Evader:** Tries to escape from the pursuer.

## **🏗️ Environment**
The simulation is built using **TurtleBotTag**, a custom environment that follows the **OpenAI Gym** interface.  
- **Grid Size:** `20x20`
- **Obstacles:** Placed in a predefined pattern.
- **Start Positions:** Both the pursuer and evader start at **random** positions in each episode.

## **🧠 Q-Learning Algorithm**
Both agents (pursuer & evader) learn their strategies using **Q-learning** with the following parameters:

| Parameter | Value |
|-----------|-------|
| **Learning rate (eta)** | `0.005` |
| **Discount factor (gamma)** | `0.9` |
| **Exploration rate (epsilon)** | `1.1` (decays over episodes) |
| **Max steps per episode** | `999` |
| **Total episodes** | `200,000` |

## **🎥 Simulation & Rendering**
- The simulation runs for a set number of **episodes**.
- Each episode has a **max step limit**.
- The **environment is rendered every 50,000 episodes** to visualize the robots' movements.
- The rendering displays:
  - The **grid environment**
  - The **robots’ positions**
  - Their **fields of view**

## **🔧 Installation**
To run the simulation, install the following dependencies:

```bash
pip install numpy --user
pip install gym --user
pip install matplotlib --user
