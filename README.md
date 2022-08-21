# Reacher
This repo contains the code to solve the Reacher environment using Deep Deterministic Policy Gradient[DDPG]

# Description
![alt text](https://github.com/kwquan/Reacher/blob/main/reacher.png)

In this notebook[Reacher.ipynb], we shall solve the Reacher environment using Deep Deterministic Policy Gradient. \
Some of the code is derived from this repository here[https://github.com/enginBozkurt/Deep-Reinforcement-Learning-for-Enterprise-Nanodegree/tree/master/Project%202%20-Continuous%20Control]. \
I removed parts of it & added some of my Pong DQN code to make it simpler, along with my own explanations. \
This is used on the latest Reacher version[V4]

Aim: \
&emsp; Reacher consists of a robotic arm controlled by our agent, whose aim is to reach the target[touching with it's tip] by applying torques on it's 2 joints \

Observation space: \
&emsp; 11 state variables

Rewards: \
&emsp;               

# Notes
If skip training, please download the pre-trained weights[reacher_actor.pth & reacher_critic.pth] before running all sections[expect 'Train agent' & 'Save model weights'] \
In addition, please download memory.py & models.py before running the code

# Documentation
