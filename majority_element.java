class Solution {
    public int majorityElement(int[] nums) {
        int a;
        int n=(nums.length/2)+1;
        HashMap <Integer,Integer> c= new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if (c.containsKey(nums[i])){
                a=c.get(nums[i])+1;
               
            }
            else{
                a=1;
            }
            c.put(nums[i],a);
            if(a==n)
               return nums[i];
        }
    
        return -1;
        
    }
}