class Solution {
    public int mySqrt(int x) {
        int low = 0, high = x, ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2; 

            long check = (long) mid * mid;

            if (check == x) {
                return mid;
            } else if (check > x) {
                high = mid - 1;
            } else {
                ans = mid; 
                low = mid + 1;
            }
        }
        return ans;
    }
}