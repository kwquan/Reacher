# Reacher
This repo contains the code to solve the Reacher environment using Deep Deterministic Policy Gradient[DDPG]

# Description
![alt text](https://github.com/kwquan/Reacher/blob/main/reacher.png)

In this notebook[Reacher.ipynb], we shall solve the Reacher environment using Deep Deterministic Policy Gradient. \
Some of the code is derived from this repository here[https://github.com/enginBozkurt/Deep-Reinforcement-Learning-for-Enterprise-Nanodegree/tree/master/Project%202%20-Continuous%20Control]. \
I removed parts of it & added some of my Pong DQN code to make it simpler, along with my own explanations. \
This is used on the latest Reacher version[V4]

Aim: \
&emsp; Reacher consists of a robotic arm controlled by our agent, whose aim is to reach the target by applying torques on \
&emsp; it's 2 joints 

Observation space: \
&emsp; 11 state variables

Rewards: \
&emsp;               

# Notes
If skip training, please download the pre-trained weights[reacher_actor.pth & reacher_critic.pth] before running all sections[expect 'Train agent' & 'Save model weights'] \
In addition, please download memory.py & models.py before running the code

# Memory
Our agent makes use of experience replay for model training. In order to achieve this, we must first store it's experiences. 

![alt text](https://github.com/kwquan/Reacher/blob/main/deque.png)

We do this by using deque. \
Deque[double-ended queue] stores elements subject to a maximum length. In our code, we use a maxlen of 50000. This means that only the latest 50000 elements are kept. In the above image, suppose that our deque already contains 50000 elements. Adding a 50001st element will lead to dropping of the 1st element since only the latest 50000 elements are kept. 

![alt text](https://github.com/kwquan/Reacher/blob/main/experience.png)

We store experiences using a namedtuple called Experiece. This creates a tuple with the following variables as shown above. Respective values are assigned before the whole tuple is appended to the deque created above. 

![alt text](https://github.com/kwquan/Reacher/blob/main/buffer.png)

Hence, memory buffer will look like the above

# Documentation
