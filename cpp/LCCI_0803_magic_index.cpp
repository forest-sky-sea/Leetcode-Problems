class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
      int i = 0, j = nums.size() -1;

      return binarySearch(i, j, nums);
    }
    int binarySearch(int i, int j, vector<int>& nums) {
      if (j < 0 || i >= nums.size() || i > j)
        return -1;
      int mid = (i + j) / 2;
      int left = binarySearch(i, mid - 1, nums);
      if (left != -1) {
        return left;
      } else if (nums[mid] == mid) {
        return mid;
      } else {
        return binarySearch(mid+1, j, nums);
      }
    }
};
