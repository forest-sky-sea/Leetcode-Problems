# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_dict = {}

        def dfs(_root: TreeNode):
            if not _root:
                return
            if _root.left:
                parent_dict[_root.left.val] = _root
                dfs(_root.left)
            if _root.right:
                parent_dict[_root.right.val] = _root
                dfs(_root.right)

        dfs(root)
        parent_set = set()
        while p:
            parent_set.add(p.val)
            p = parent_dict.get(p.val)
        while q:
            if q.val in parent_set:
                return q
            q = parent_dict.get(q.val)
        return root


tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(1)))
