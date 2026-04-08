class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        start = []
        for i in range(len(position)):
            start.append((position[i], speed[i]))
        
        start = sorted(start, key=lambda element: element[0], reverse=True)

        arrival = None
        output = 0
        for (p, v) in start:
            if arrival == None:
                arrival = (target - p) / v
                output += 1
            else:
                temp = max(arrival, ((target - p) / v))
                if temp != arrival:
                    arrival = temp
                    output += 1

        return output
            