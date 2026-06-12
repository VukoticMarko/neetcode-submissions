class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""

        for s in strs:
            encode += str(len(s)) + "#" + s

        return encode



    def decode(self, s: str) -> List[str]:

        decode = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+1+length]

            decode.append(word)

            i = j + 1 + length

        return decode
