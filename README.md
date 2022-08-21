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

### Storing experiences
Our agent makes use of experience replay for model training. In order to achieve this, we must first store it's experiences. 

![alt text](https://github.com/kwquan/Reacher/blob/main/deque.png)

We do this by using deque. \
Deque[double-ended queue] stores elements subject to a maximum length. In our code, we use a maxlen of 50000. This means that only the latest 50000 elements are kept. In the above image, suppose that our deque already contains 50000 elements. Adding a 50001st element will lead to dropping of the 1st element since only the latest 50000 elements are kept. 

### Set experience as namedtuple
![alt text](https://github.com/kwquan/Reacher/blob/main/experience.png)

We store experiences using a namedtuple called Experiece. This creates a tuple with the following variables as shown above. Respective values are assigned before the whole tuple is appended to the deque created above. 

![alt text](https://github.com/kwquan/Reacher/blob/main/buffer.png)

Hence, memory buffer will look like the above

### Sampling experiences
![alt text](https://github.com/kwquan/Reacher/blob/main/sample.png)

If sampling is called, we iterate through the tuples & split them to their respective arrays. Note that all arrays will have the same size[batch_size] & each element is from a separate experience.

# Weights Update

### Process
![alt text](https://github.com/kwquan/Reacher/blob/main/model.png)

There are 2 parts to updating weights. \
1st part requires action selection from the current state. This is achieved by passing state variables to actor model. The action output will be combined with the state variables & passed to critic model to compute our state-action value. 

2nd part requires next action selection given next state. This is achieved by passing next state variables to actor TARGET model. The next action output will be combined with the next state variables & passed to critic TARGET model to compute our next state-action value. 

We then calculate target state-action value[refer to above]. Finally, mse loss is calculated using state-action value & target state-action value before doing back-propagation.

# Documentation
