from datetime import datetime
from random import randint as rs
from math import modf

class Invwk(object):

    def __init__(self, scope=20):
        self.scope = scope
        self.max = pow(2, 32)


    def get_random(self):
        seed = rs(1, self.max)

        # Shift off bits, discarding the sign.Discarding the sign is
        # important because OR w / 5 can give us + or - numbers.

        seed += (seed * seed) | 5

        r = (seed >> 32) / self.max

        return int(modf(r)[0] * 10000000) % self.scope

