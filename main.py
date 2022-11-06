"""
REQUIREMENTS:

python.__version__      : 3.9.2
numpy.__version__       : 1.19.5
matplotlib.__version__  : 3.3.4

Author: Ntigkaris Alexandros
"""

if __name__ == "__main__":

    from utils import BatColony

    config = {
                "entities":15,
                "timesteps":10,
                "alpha":0.9,
                "gamma":0.9,
                "verbose":True,
                "random_state":2036,
                "sleep_rate":1e-10,
            }

    bats = BatColony(**config)
    bats.fill()
    bats.run()