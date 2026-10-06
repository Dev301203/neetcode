class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += chr(len(i)) + i
        return encoded


    def decode(self, s: str) -> List[str]:
        pointer = 0
        decoded = []
        while pointer < len(s):
            length = ord(s[pointer])
            pointer += 1
            decoded.append(s[pointer:pointer+length])
            pointer += length
        return decoded

        

