/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
	int height_l;
    int height_r;
    
	if (!root)
		return (0);

	height_l = maxDepth(root->left);
	height_r = maxDepth(root->right);
	return (height_l > height_r ? height_l + 1: height_r + 1);
}