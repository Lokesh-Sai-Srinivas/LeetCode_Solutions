class Solution:
    precomputed = {}

    for h in range(12):
        for m in range(60):
            bits = bin(h).count("1") + bin(m).count("1")
            time_str = f"{h}:{m:02d}"
            if bits not in precomputed:
                precomputed[bits] = []
            precomputed[bits].append(time_str)

    def readBinaryWatch(self, turnedOn: int):
        return Solution.precomputed.get(turnedOn, [])
