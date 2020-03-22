import gym
from baselines.baselines import deepq
from baselines.baselines.common import models


def main():
    """
    Training and saving a model using deepq-learning in the mountaincar environment.
    """
    env = gym.make("MountainCar-v0")
    # Enabling layer_norm here is import for parameter space noise!
    act = deepq.learn(
        env,
        network=models.mlp(num_hidden=64, num_layers=1),
        lr=1e-3,
        total_timesteps=100000,
        buffer_size=50000,
        exploration_fraction=0.1,
        exploration_final_eps=0.1,
        print_freq=10,
        param_noise=True
    )
    print("Saving model to mountaincar_model.pkl")
    act.save("mountaincar_model.pkl")


if __name__ == '__main__':
    main()
