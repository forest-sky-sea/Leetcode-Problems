/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
  // unordered_map<Node*, Node*>visited;
    Node* visited[101]{nullptr};
    // unordered_map<int, Node*>visited;
    Node* cloneGraph(Node* node) {
      if (node == nullptr) 
        return node;
      // cout << "v: " << visited[node] << endl;
      if(visited[node->val] != nullptr) {
        return visited[node->val];
      }

      Node* cloned_node = new Node(node->val);
      visited[node->val] = cloned_node;
      for (int i = 0 ; i < node->neighbors.size(); i++) {
        cloned_node->neighbors.emplace_back(cloneGraph(node->neighbors[i]));
      }
      return cloned_node;
    }
};
