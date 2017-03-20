#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};


struct Node* NewNode(int data){
	struct Node* new_node = (struct Node *)malloc(sizeof(struct Node));
	new_node->data =data;
	new_node->left = NULL;
	new_node->right = NULL;
	return new_node;
}

void inorder_traverse(struct Node* root){
	if(root == NULL)
		return;
	inorder_traverse(root->left);
	printf("%d ", root->data);
	inorder_traverse(root->right);
}


int Height(struct Node* node){
	if(node == NULL)
		return 0;
	int lheight = Height(node->left);
	int rheight = Height(node->right);
	return lheight>rheight? lheight+1:rheight+1;
}


int IsBalanced(struct Node* node){
	// complexity: O(n^2)
	if(node==NULL)
		return 1;
	if(node->left==NULL && node->right == NULL)
		return 1;
	else{
		int balance_factor = Height(node->left)-Height(node->right);
		if(balance_factor >=-1 && balance_factor <=1){
			return IsBalanced(node->left) && IsBalanced(node->right);
		}
	}
	return 0;
}

int IsBalancedRecursion(struct Node* node, int* h){
	// Optimized 
	// complexity: O(n)
	int lh=0, rh=0;
	int l=0, r=0;
	if(node == NULL){
		*h = 0;
		return 1;
	}
	l = IsBalancedRecursion(node->left, &lh);
	r = IsBalancedRecursion(node->right, &rh);
	*h = lh >rh ? lh+1 : rh+1;
	if((lh-rh > 1 ) || (lh-rh < -1))
		return 0;
	else
		return l && r;
}


int main(){

	struct Node* new_node_1 = NewNode(4);
	struct Node* root = new_node_1;
	root->left = NewNode(3);
	root->right = NewNode(6);
	root->left->left = NewNode(2);
	// /root->left->left->left = NewNode(1);
	root->right->left = NewNode(5);
	root->right->right = NewNode(7);
	inorder_traverse(root);
	printf("\n************\n");
	printf("%d\n", IsBalanced(root));
	int height = 0;
	printf("%d\n", IsBalancedRecursion(root, &height));


	// create tree 1
	struct Node* tree1_node_1 = NewNode(26);
	struct Node* root_1 = tree1_node_1;
	root_1->left = NewNode(10);
	root_1->right = NewNode(3);
	root_1->right->right = NewNode(3);
	root_1->left->left = NewNode(4);
	root_1->left->right = NewNode(6);
	inorder_traverse(root_1);
	printf("\n************\n");

	// create tree 2
	struct Node* tree2_node_1 = NewNode(1);
	struct Node* root_2 = tree2_node_1;
	root_2->left = NewNode(3);
	root_2->left->right = NewNode(6);
	root_2->right = NewNode(2);
	root_2->right->left = NewNode(4);
	root_2->right->right = NewNode(5);
	root_2->right->right->left = NewNode(8);
	root_2->right->right->right = NewNode(7);
	inorder_traverse(root_2);

}