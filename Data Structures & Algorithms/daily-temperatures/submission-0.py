class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = (temperatures[-1], len(temperatures)-1)
        s = []
        s.append(temp)
        results = []
        results.append(0)
        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] < s[-1][0]:
                results.append(s[-1][1]-i)
                s.append((temperatures[i], i))
            else:
                while s and temperatures[i] >= s[-1][0]:
                    s.pop()
                if not s:
                    results.append(0)
                else:
                    results.append(s[-1][1]-i)
                s.append((temperatures[i], i))


        results.reverse()
        return results