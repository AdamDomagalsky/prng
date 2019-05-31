from datetime import datetime


class Wichmann_Hill(object):
    time_seed = staticmethod(
        lambda: (
                        int((datetime.now() - datetime(1970, 1, 1)).total_seconds())
                        +
                        datetime.now().microsecond
                )
    )

    def __init__(self, scope=20):
        self.scope = scope

    def get_random(self):
        seed = Wichmann_Hill.time_seed()
        _s1 = seed
        _s2 = seed + 1
        _s3 = seed + 2

        self.s1 = 171 * (_s1 % 177) - 2 * (_s1 // 177)
        if (self.s1 < 0):
            self.s1 += 30269
        self.s2 = 172 * (_s2 % 176) - 35 * (_s2 // 176)
        if (self.s2 < 0):
            self.s2 += 30307
        self.s3 = 170 * (_s3 % 178) - 63 * (_s3 // 178)

        if (self.s3 < 0):
            self.s3 += 30323

        self.r = (self.s1 / 30269.0 + self.s2 / 30307.0 + self.s3 / 30323.0) % 1
        from math import modf

        return int(modf(self.r)[0] * 10000000) % self.scope
