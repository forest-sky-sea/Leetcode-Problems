class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() == 0) {
        
            int len = nums2.size();
            int mid = len / 2;
            if ((len % 2) == 0) 
                return (nums2[mid] + nums2[mid - 1]) / 2.0;
            else
                return nums2[mid];
        }

        if (nums2.size() == 0) {
            int len = nums1.size();
            int mid = len / 2;
            if (len % 2 == 0) 
                return (nums1[mid] + nums1[mid - 1]) / 2.0;
            else
                return nums1[mid];
        }

        int len1 = nums1.size();
        int len2 = nums2.size();
        int mid = (len1 + len2) / 2;
        int idx = 0, i = 0, j = 0;
        int last = 0, temp =0;

        while(idx <= mid) {
            idx ++;
            last = temp;
            if (i == len1) {
                temp = nums2[j];
                j++;
                continue;
            }

            if (j == len2) {
                temp = nums1[i];
                i++;
                continue;
            }

            if(nums1[i] <= nums2[j]) {
                temp = nums1[i];
                i++;
            } else {
                temp = nums2[j];
                j++;
            }
        }
        
        if((len1 + len2) % 2 == 0) {
            return (last + temp) / 2.0;
        } else {
            return temp;
        }
        
    }
};
