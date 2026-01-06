class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (!root->left && !root->right)
            return 1;
        long long maxSum = LLONG_MIN;
        int ans = 1, currLevel = 1;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            long long currSum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                currSum += node->val;
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            if (currSum > maxSum) {
                maxSum = currSum;
                ans = currLevel;
            }
            currLevel++;
        }
        return ans;
    }
};