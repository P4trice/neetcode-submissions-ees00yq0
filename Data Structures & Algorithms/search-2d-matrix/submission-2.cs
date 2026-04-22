public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // first we search the row based on the first entry of each row
        // we also have to make sure it's not smaller than the first entry 
        // and not larger than the last
        // after finding the row, we find the exact element using binary search

        if(target < matrix[0][0] || target > matrix.Last().Last())
        {
            return false;
        }
        else 
        {
            var lo = 0;
            var hi = (matrix.Length * matrix[0].Length) - 1;
            while (lo <= hi) 
            {
                var mid = (int)Math.Ceiling((float)((lo + hi) /2));
                int row = mid / matrix[0].Length;
                int col = mid % matrix[0].Length;
                if (matrix[row][col] == target)
                {
                    return true;
                }
                else if (matrix[row][col] < target) 
                {
                    lo = mid + 1;
                }
                else if (matrix[row][col] > target)
                {
                    hi = mid - 1;
                }
            }
            return false;
        }
    }
}
