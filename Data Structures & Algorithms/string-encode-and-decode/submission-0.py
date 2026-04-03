class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + '#' + string
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            str_len = ''
            while s[i] != '#':
                str_len += s[i]
                i += 1
            str_len = int(str_len)
            i += 1 #Moving forward to ignore the #
            decode_list.append(s[i:i+str_len])
            i += str_len
        return decode_list



