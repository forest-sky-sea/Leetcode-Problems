class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int tmp = nums[0];
        int i = 1;
        int j = 1;
        for ( ; j < nums.size(); j++) {
            if (nums[j] != tmp) {
                tmp = nums[j];
                nums[i++] = nums[j]; 
            }
        }
        return i;
    }
};
