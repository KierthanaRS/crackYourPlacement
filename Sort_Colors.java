import java.util.Arrays;
import java.util.Scanner;
class Solution {
    public void sortColors(int[] nums) {
        Arrays.sort(nums);
    }
    public static void main(String[] args){
        Solution sol=new Solution();
        Scanner item=new Scanner(System.in);
        int n= item.nextInt();
        int[] nums= new int[n];
        for(int i=0;i<n;i++){
            nums[i]=item.nextInt();
        }
        sol.sortColors(nums);
        System.out.println(Arrays.toString(nums));

        
    }
}