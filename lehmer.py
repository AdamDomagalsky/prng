from datetime import datetime

class Lehmer(object):

    time_seed = staticmethod(
        lambda: (
                        int((datetime.now() - datetime(1970, 1, 1)).total_seconds())
                        +
                        datetime.now().microsecond
                )
    )

    def __init__(self, scope=20):
        self.scope = scope
        self.A = 16807
        self.M = 2147483647
        self.Q = 127773
        self.R = 2836

    def get_random(self):
        seed = Lehmer.time_seed()
        hi = seed / self.Q
        lo = seed % self.Q
        seed = (self.A * lo) - (self.R * hi)
        if(seed < 1):
            seed += self.M
        r = ((1.0 * seed) / self.M) % self.scope
        from math import modf
        return int(modf(r)[0] * 10000000) % self.scope


