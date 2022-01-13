from models import Actor
import torch as t
import yaml
import gym
if __name__ == "__main__":
    with open("./SoftActorCritic(SAC)/SoftActorCritic/settings.yaml", "r", encoding="utf-8") as f:
        args = yaml.load(f.read(), Loader=yaml.FullLoader)
    env = gym.make(args["env_name"])

    actor = Actor(
        env.observation_space.shape[0],
        env.action_space.shape[0],
        args["hiddenlayer_size"],
        args["log_std_max"],
        args["log_std_min"],
        args["lr_actor"],
        env.action_space.high,
        args["cuda"],
    )

    actor.load_state_dict(t.load(args["actor_model_dir"]))
    for ep in range(10):
        done = False
        obs = env.reset()
        reward_sum = 0
        while not done:
            env.render()
            with t.no_grad():
                obs_tensor = t.tensor(obs, device=actor.device).unsqueeze(0)
                mean, _ = actor.forward(obs_tensor)
                actions = t.tanh(mean).cpu().detach().numpy()[0]
            obs_, reward, done, _ = env.step(actions)
            reward_sum += reward

            obs = obs_

    print("episode:{},reward:{}".format(ep+1, reward_sum/(ep+1)))
