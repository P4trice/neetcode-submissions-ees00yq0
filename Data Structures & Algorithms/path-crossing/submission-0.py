class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        current = (0,0)
        visited.add(current)

        for i in path:
            if i == 'N':
                current = (current[0], current[1]+1)
            if i == 'S':
                current = (current[0], current[1]-1)
            if i == 'W':
                current = (current[0]-1, current[1])
            if i == 'E':
                current = (current[0]+1, current[1])
            if current in visited:
                return True
            visited.add(current)
        return False