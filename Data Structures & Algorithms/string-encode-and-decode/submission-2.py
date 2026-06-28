class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            i = end
            
        return res