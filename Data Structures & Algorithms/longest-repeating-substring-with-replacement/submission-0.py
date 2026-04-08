class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_freq = s[0]
        freq_dict = {}
        size = 0
        for j in range(len(s)):
            if s[j] not in freq_dict:
                freq_dict[s[j]] = 1
            else:
                freq_dict[s[j]] += 1
            if  freq_dict[s[j]] > freq_dict[max_freq]:
                max_freq = s[j]
            if not (j - i + 1) - freq_dict[max_freq] <= k:
                freq_dict[s[i]] -= 1
                i += 1
            size = max(size, j - i + 1)

        return size