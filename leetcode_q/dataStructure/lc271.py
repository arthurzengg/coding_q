class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_string = ''
        for string in strs:
            encode_string += str(len(string)) + '#' + string
            print(encode_string)
        return encode_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return res
