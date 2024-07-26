class Solution {
    public int maxProfit(int[] prices) {
       int mincost=Integer.MAX_VALUE;
       int profit=0;
       for(int cost:prices){
          if(cost<mincost) mincost=cost;
          profit=Math.max(profit,cost-mincost);
       }
        return profit;
    }
}