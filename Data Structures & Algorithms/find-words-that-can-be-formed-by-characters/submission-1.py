class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            copy = chars
            flag = False
            for char in word:
                if char not in copy:
                    flag = True
                else:
                    copy = copy.replace(char, '', 1)
            if flag == False:
                count += len(word)

        return count
            