import code
import hp
import zombie
import hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
