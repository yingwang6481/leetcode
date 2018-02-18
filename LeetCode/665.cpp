class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool use_modify = false;
        for(int i=0, pre=nums[0];i<nums.size();++i){
            if(nums[i]<pre && use_modify++) return false;
            if(nums[i]<pre && i>=2 && nums[i-2] >nums[i]) continue;
            pre = nums[i];
        }
        return true;
    }
};
