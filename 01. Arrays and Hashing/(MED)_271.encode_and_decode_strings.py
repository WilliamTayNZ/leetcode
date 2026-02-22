from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]

        return encoded
        

    def decode(self, s: str) -> List[str]:
        # Example encoded string: 3#de$5#i98*e2#ab
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + 1 + length

        return decoded

    
codec = Codec()
print(codec.decode(codec.encode(["Hello","World"])))
print(codec.decode(codec.encode([""])))
print(codec.decode(codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])))