from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        '''#old solution that is O(n^3) so I had to redo it
        differences = []
        for begin in range (len(s)):
            for end in range (begin+k, len(s)+1):
                subs = s[begin:end]        
                occurances = dict()
                for i in range(len(subs)):
                    if subs[i] in occurances.keys():
                        occurances[subs[i]] += 1
                    else:
                        occurances[subs[i]] = 1
                largest_odd = 0
                smallest_even = len(subs) + 1
                for key, count in occurances.items():
                    if count % 2 == 0:
                        # even
                        if count < smallest_even:
                            smallest_even = count
                    else:
                        # odd
                        if count > largest_odd:
                            largest_odd = count
                differences.append(largest_odd - smallest_even)
        return max(differences)'''


        ans = -inf
        for a in '01234':
            for b in '01234':
                if a != b:
                    seen = defaultdict(lambda: inf)
                    pa = [0] # this is the full list of the number of times a appears before and at the index it's stored at
                    pb = [0]
                    start = 0
                    for index, value in enumerate(s):
                        pa.append(pa[-1])
                        pb.append(pb[-1])
                        if value == a: pa[-1] += 1
                        elif value == b: pb[-1] += 1
                        while start <= index+1 - k and pa[start] < pa[-1] and pb[start] < pb[-1]:
                            key = (pa[start] % 2, pb[start] % 2)
                            diff = pa[start] - pb[start]
                            seen[key] = min(diff, seen[key])
                            start += 1
                        key = (1 - pa[-1]%2, pb[-1]%2) # this ensures that the substring has a as odd and b as even
                        diff = pa[-1] - pb[-1]
                        ans = max(ans, diff - seen[key])
        return ans

