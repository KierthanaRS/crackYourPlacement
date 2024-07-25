import java.util.Scanner;
import java.util.Arrays;
class RemoveDuplicate {
    public int removeDuplicates(int[] nums) {
        int j=0;
        for(int i=1;i<nums.length;i++){
            if(nums[j]==nums[i]){
                continue;
            }
            else{
                j++;
                nums[j]=nums[i];
            }
        }
        return j+1;
        
    }
    public static void main(String[] args){
        RemoveDuplicate rd=new RemoveDuplicate();
        Scanner item=new Scanner(System.in);
        int n=item.nextInt();
        int[] nums=new int[n];
        for(int i=0;i<n;i++) nums[i]=item.nextInt();
        int ans=rd.removeDuplicates(nums);
        System.out.println(Arrays.toString(Arrays.copyOf(nums, ans)));
    }
}