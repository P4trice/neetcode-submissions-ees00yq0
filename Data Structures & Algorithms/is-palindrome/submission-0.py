class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned = cleaned.lower()
        list(cleaned)
        print(cleaned)
        # remove anything non alphanumerical (spaces, kommas, points, etc.)
        # turn everything lowercase

        #move one pointer from front to back
        #move one pointer from back to front
        #check if they're same
        for i in range(math.ceil(len(cleaned)/2)):
            if not (cleaned[i] == cleaned[len(cleaned) - i - 1]):
                return False

        return True