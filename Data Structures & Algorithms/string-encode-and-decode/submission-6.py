class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output = output + "#" + str(len(s)).zfill(4) + s
        print("output: " + output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while s:
            num = int(s[1:5])
            output.append(s[5:5+num])
            print("num: " + s[1:5])
            print("word: " + s[5:5+num])
            s = s[5+num:]
        return output