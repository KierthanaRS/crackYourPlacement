#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0,r=height.size()-1,h;
        int area=0;
        while(l<r){
            h=min(height[l],height[r]);
            area=max(area,(r-l)*h);
            if(height[l]>=height[r])
               r--;
            else l++;
        }
        return area;
    }
};