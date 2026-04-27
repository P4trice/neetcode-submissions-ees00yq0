public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        if (h == piles.Count()){
            return piles.Max();
        }
        var lo = 1;
        var hi = piles.Max();
        var possible = int.MaxValue;
        while (lo < hi)
        {
            var mid = (hi + lo) /2;
            var steps = ExecuteWithMid(piles, mid);
            if (steps <= h){
                possible = mid;
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return possible;
    }

    public int ExecuteWithMid(int[] piles, int mid) {
        int steps = 0;
        for(int i = 0; i < piles.Count(); i++){
            steps += (piles[i] + mid - 1) / mid;
        }
        return steps;
    }
}
