class Solution {
    public int[] productExceptSelf(int[] nums) {

        int size = nums.length;

        int[] left_product = new int[size];
        int[] right_product = new int[size];
        int[] ans = new int[size];

        for(int i = 0; i < size; i++){
            if(i == 0){
                left_product[i] = 1;
                right_product[i] = 1;
                continue;
            }

            left_product[i] = left_product[i - 1] * nums[i - 1];

            right_product[i] = right_product[i - 1] * nums[size - i];
        }


        for(int i = 0; i < size; i++){
            ans[i] = left_product[i] * right_product[size - 1 - i];
        }

        return ans;
        
    }
}
