register(
    id='FrozenLake8x6-v0',
    entry_point='gym_frozen.envs:FrozenLakeEnv',
    kwargs={'map_name' : '8x6'},
    max_episode_steps=200,
    reward_threshold=0.99, # optimum = 1
)
