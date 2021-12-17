# 强化学习

## 进度

|   method    | done |
| :---------: | ---- |
| Qlearnling  | √    |
|    Sarsa    | √    |
| SarsaLambda | √    |
|     DQN     | √    |
|     PG      | √    |
| ActorCritic | √    |
|    ACER     | √    |
| DuelingDQN  | √    |
| DQNwithPER  | √    |
|    DDPG     | √    |
|     TD3     | ×    |
|     A3C     | √    |
|     A2C     | ×    |
|     PPO     | √    |
|    DPPO     | ×    |
|     SAC     | ×    |
| DQNwithHER  | ×    |
| DDPGwithHER | ×    |
|    DIAYN    | ×    |

---

## Qlearning

更新一个 Q 表，表中的每个元素代表每个状态下每个动作的潜在奖励<br>
根据 Q 表选择动作，然后更新 Q 表

```
state 1 2 3 4 5
left  0 0 0 0 0
right 0 0 0 1 0
```

更新策略：`现实值=现实值+lr*（估计值-现实值）`

---

## Sarsa

Qlearning 更新方法：`根据当前Q表选择动作->执行动作->更新Q表`<br>
Sarsa 更新方法：`执行动作->根据当前估计值选择下一步动作->更新Q表`

**Sarsa 是行动派，Qlearning 是保守派**

---

## SarsaLambda

Sarsa 的升级版<br>
Qlearning 和 Sarsa 都认为上一步对于成功是有关系的，但是上上一步就没有关系了，SarsaLambda 的思想是：`到达成功的每一步都是有关系的，他们的关系程度为：越靠近成功的步骤是越重要的`<br>

```
step
1-2-3-4-5-success
重要性1<2<3<4<5
```

---

## DQN

![](./DeepQLearningNetwork/dqn.jpg)<br>
用神经网络代替 Q 表的功能

Q 表无法进行所有情况的枚举，在某些情况下是不可行的，比如下围棋。<br>
Features: `Expericence Replay and Fixed Q-targets`

Experience Replay : `将每一次实验得到的惊艳片段记录下来，然后作为经验，投入到经验池中，每次训练的时候随机取出一个 BATCH，可以复用数据。`

Fixed Q-target: `在神经网络中，Q 的值并不是互相独立的，所以不能够进行分别更新操作，那么我们需要将网络参数复制一份，解决该问题。`

为了解决 overestimate 的问题，引入 double DQN，算法上有一点点的改进，复制一份网络参数，两个网络的参数异步更新

---

## Policy Gradient

核心思想：让好的行为多被选择，坏的行为少被选择。<br>
采用一个参数 vt，让好的行为权重更大<br>
![](./PolicyGradient/5-1-1.png)<br>

---

## ActorCritic

使用神经网络来生成 vt，瞎子背着瘸子

---

## Dueling DQN

将 Q 值的计算分成状态值 state_value 和每个动作的值 advantage，可以获得更好的性能

---

## DQN with Prioritized Experience Replay

在 DQN 中，我们有 Experience Replay，但是这是经验是随机抽取的，我们需要让好的、成功的记忆多多被学习到，所以我们在抽取经验的时候，就需要把这些记忆优先给网络学习，于是就有了`Prioritized`Experience Replay

---

## DDPG

![](DeepDeterministicPolicyGradient\principle.png)

- Exploration noise
- Actor-Critic Achetecture
- Fixed Q-Target
- Policy Gradient
- Experience Replay (OFF-POLICY)

---

## A3C

- A3C 里面有多个 agent 对网络进行异步更新，相关性较低
- 不需要积累经验，占用内存少
- on-policy 训练
- 多线程异步,速度快

---

## PPO

- 感觉像 Actor-Critic 和 DQN 的折中，先取一部分经验，然后进行网络参数的更新
- Actor-Critic 是每走一步进行参数更新
- DQN 是直接积累经验然后从经验池子中学习
- PPO 是积累部分经验，然后进行多轮的梯度下降

## Soft Actor Critic & DQN with Hindsight Experience Relpay && Diversity Is All You Need & DDPG with Hindsight Experience Relpay

待完成

---

## Requirements

- numpy
- tensorboardX
- torch
- gym

---

## 杂谈&经验

- t.tensor.detach()： 返回 t.tensor 的数据而且 require_grad=False.torch.detach()和 torch.data 的区别是，在求导时，torch.detach()会检查张量的数据是否发生变化，而 torch.data 则不会去检查。
- with t.no_grad(): 在应用阶段，不需要使用梯度，那么可以使用这个去掉梯度
- 如果在更新的时候不调用 optimizer.zero_grad，两次更新的梯度会叠加。
- 使用 require_grad=False 可以冻结神经网络某一部分的参数，更新的时候就不能减 grad 了
- tensor.item()，直接返回一个数据，但是只能适用于 tensor 里头只有一个元素的情况，否则要是用 tolist()或者 numpy()
- 不建议使用 inplace 操作
- hard replacement 每隔一定的步数才更新全部参数，也就是将估计网络的参数全部替换至目标网络而 soft replacement 每一步就更新，但是只更新一部分(数值上的一部分)参数。
- pytorch 官网上有:https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

## 引用

[莫烦 python](https://mofanpy.com/)

[《动手学深度学习》](https://zh-v2.d2l.ai/)

[17 种深度强化学习算法用 Pytorch 实现](https://blog.csdn.net/tMb8Z9Vdm66wH68VX1/article/details/100975138?spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-14.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-14.no_search_link)

[hhy_csdn 博客](https://blog.csdn.net/hhy_csdn)

[OpenAI Gym](https://gym.openai.com/)
