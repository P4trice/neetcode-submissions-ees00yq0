class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        seen = {}
        for i in required:
            seen[i] = []
        best = ""

        def is_valid():
            for c in required:
                if required[c] > len(seen[c]):
                    return False
            return True

        def get_min_front():
            temp_idx = float('inf')  # safer than hardcoding 2000
            temp_char = None
            for c in required:
                if seen[c][0] < temp_idx:
                    temp_idx = seen[c][0]
                    temp_char = c
            return temp_idx, temp_char

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]].append(i)

            # shrink as long as window is valid
            while is_valid():
                # window boundaries
                left, _ = get_min_front()
                right = -1
                for c in required:
                    right = max(right, seen[c][-1])
                window = s[left:right+1]

                if best == "" or len(window) < len(best):
                    best = window

                # pop the left boundary to try shrinking
                _, min_char = get_min_front()
                seen[min_char].pop(0)

        return best
        