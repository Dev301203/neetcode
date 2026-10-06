class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)
        for string in strs:
            str_bitmap = [0]*26
            for ch in string:
                str_bitmap[ord(ch) - ord('a')] += 1
            str_bitmap = tuple(str_bitmap)
            values[str_bitmap].append(string)
        return list(values.values())
