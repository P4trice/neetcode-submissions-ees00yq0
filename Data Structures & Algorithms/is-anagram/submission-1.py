class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_prime = list(s)
        s_prime.sort()
        t_prime = list(t)
        t_prime.sort()
        for i in range(max(len(s), len(t))):
            if i >= min(len(s), len(t)):
                return False
            if not s_prime[i] == t_prime[i]:
                return False
        return True