class Solution {
public:
    int integerBreak(int n) {
      int dic[] = {0, 0, 1, 2, 4, 6, 9};
      if (n < 7) {
        return dic[n];
      } 

      if (n % 3 == 0) {
        return (int)pow(3.0, n/3);
      }

      if ((n - 2) % 3 == 0) {
        return (int)2*pow(3.0, (n-2)/3);
      }

      if ((n - 4) % 3 == 0) {
        return (int)4*pow(3.0, (n-4)/3);
      }
    }
};
