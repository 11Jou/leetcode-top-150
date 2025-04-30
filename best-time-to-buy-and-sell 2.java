import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int maxProfit(int[] prices) {
        int totalProfit = 0;

        for (int i = 0 ; i < prices.length - 1; i++){
            int price = prices[i];
            int profit = prices[i+1] - price;

            if (profit > 0){
                totalProfit += profit;
            }
        }

        return totalProfit;

        
    }
}