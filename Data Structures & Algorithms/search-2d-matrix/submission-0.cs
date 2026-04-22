public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // first we search the row based on the first entry of each row
        // we also have to make sure it's not smaller than the first entry 
        // and not larger than the last
        // after finding the row, we find the exact element using binary search

        int[] joined = matrix[0];
        for(int i = 1; i < matrix.Length; i++)
        {
            joined = joined.Concat(matrix[i]).ToArray();
        }

        if(target < joined[0] || target > joined.Last())
        {
            return false;
        }
        else 
        {
            var lo = 0;
            var hi = joined.Length - 1;
            while (lo <= hi) 
            {
                var mid = (int)Math.Ceiling((float)((lo + hi) /2));
                if (joined[mid] == target)
                {
                    return true;
                }
                else if (joined[mid] < target) 
                {
                    lo = mid + 1;
                }
                else if (joined[mid] > target)
                {
                    hi = mid - 1;
                }
            }
            return false;
        }
    }
}
