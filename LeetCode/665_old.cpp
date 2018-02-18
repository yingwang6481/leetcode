class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool use_modify = false;
        for(int i=0; i<nums.size()-1; ++i){
            if(nums[i]>nums[i+1]){
                if(use_modify) return false;
                int a = (i==0)?1:nums[i-1];
                int c = nums[i+1];
                if(a<=c){
                    use_modify = true;
                    continue;
                }
                int d = (i==nums.size()-2)?10000:nums[i+2];
                int b = nums[i];
                if(b<=d){
                    use_modify = true;
                    ++i;
                    continue;
                }
                return false;
            }
        }
        return true;
    }
};
