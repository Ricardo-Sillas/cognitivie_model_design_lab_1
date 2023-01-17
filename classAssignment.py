import pyibl
import random

import matplotlib.pyplot as plt

from tqdm import tqdm

PARTICIPANTS = 100
ROUNDS = 100
NOISE = 0.25
DECAY = 0.5
DEFAULT_UTILITY = 10


def run(rounds, participants):
    best_chosen = [0] * rounds
    a = pyibl.Agent(default_utility=DEFAULT_UTILITY, noise=NOISE, decay=DECAY)
    for p in tqdm(range(participants)):
        a.reset()
        a.trace =True
        for r in range(rounds):
            c = a.choose("A", "B")
            if c == "B":
                a.respond(3.0)
            elif random.randint(0,10) <= 8.0:
                best_chosen[r] += 1
                a.respond(4.0)
            else:
                a.respond(0)
        a.instances()
    return [n / participants for n in best_chosen]


def main():
    plt.plot(range(1, ROUNDS + 1), run(ROUNDS, PARTICIPANTS))
    plt.ylim([0, 1])
    plt.ylabel("fraction choosing the best option")
    plt.xlabel("round")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
