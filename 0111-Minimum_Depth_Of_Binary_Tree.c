/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root){
	int height_l;
    int height_r;
    
	if (!root)
		return (0);
    
	height_l = minDepth(root->left);
	height_r = minDepth(root->right);
	return (height_l < height_r && root->left || !root->right ? height_l + 1: height_r + 1);
}