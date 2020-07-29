class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        int i = 0;
        int j = height.size() -1;
        int temp = 0;
        while (i != j) {
            if (height[i] < height[j]) {
                temp = height[i] * (j-i);
                i++;
            } else {
                temp = height[j] * (j-i);
                j--;
            }
            if (temp > res)
                res = temp;
        }
        return res;
    }
};