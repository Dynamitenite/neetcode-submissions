class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}

        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        max_odd = 0
        min_even = float('inf')

        for freq in counts.values():
            if freq % 2 == 0:
                if freq < min_even:
                    min_even = freq
            else:
                if freq > max_odd:
                    max_odd = freq

        return max_odd - min_even
