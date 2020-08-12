/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int result = 0;
    unordered_map<TreeNode*, int> temp;
    int rob(TreeNode* root) {  
      if(root == nullptr) 
            return 0;
        if(root->left == nullptr && root->right == nullptr)
            return root->val;
        
        if(temp[root]) 
            return temp[root];
        
        int not_rob_val = rob(root->left) + rob(root->right);
        
        int rob_val = root->val;
        if(root->left) rob_val += rob(root->left->left) + rob(root->left->right);
        if(root->right) rob_val += rob(root->right->left) + rob(root->right->right);
        temp[root] = max(not_rob_val, rob_val);
        return max(not_rob_val, rob_val);
    }
    
};
