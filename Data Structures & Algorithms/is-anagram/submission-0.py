class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        letters2 = defaultdict(int)
        for i in s:
            letters[i] += 1
        for i in t:
            letters2[i] += 1
        return letters == letters2