class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        
        if count_s1 == count_s2:
            return True

        for i in range(len(s2)-len(s1)):
            count_s2[s2[i]] -= 1
            count_s2[s2[i+len(s1)]] += 1
            
            if count_s2[s2[i]] == 0:
                del count_s2[s2[i]]
            if count_s2 == count_s1:
                return True


        return False
