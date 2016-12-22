/*
	Find all lowest nodes which terminates into K leaves

*/



#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

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

int GetNumberOfLeaves(struct Node* root){
	if(root == NULL)
		return 0;
	if (root->left == NULL && root->right ==NULL)
		return 1;
	return GetNumberOfLeaves(root->left)+GetNumberOfLeaves(root->right);
}



void FindLowestNodesWithKleaves(struct Node* node, int k){
	if(node==NULL || k==INT_MAX){
		return;
	}
	if(GetNumberOfLeaves(node) == k){
		printf("%d ", node->data);
		k = INT_MAX;
	}
	FindLowestNodesWithKleaves(node->left, k);
	FindLowestNodesWithKleaves(node->right, k);
}



int main(){
	struct Node* new_node_1 = NULL;
// 		   	4
// 		 3      5
// 	 2       6    7
// 1 
	int k = 1;    
	new_node_1 = NewNode(4);
	struct Node* root = new_node_1;
	root->left = NewNode(3);
	root->right = NewNode(5);
	root->left->left = NewNode(2);
	root->left->left->left = NewNode(1);
	root->right->left = NewNode(6);
	root->right->right = NewNode(7);
	printf("inorder_traversal:");
	inorder_traverse(root);
	printf("\n************\n");
	printf("Lowest Most Nodes with %d leaves: ",k);
	FindLowestNodesWithKleaves(root, k);
	printf("\n************\n");

	// create tree 1
	struct Node* tree1_node_1 = NewNode(1);
	struct Node* root_1 = tree1_node_1;
	root_1->left = NewNode(2);
	root_1->right = NewNode(3);
	root_1->right->left = NewNode(6);
	root_1->left->left = NewNode(4);
	root_1->left->right = NewNode(5);
	root_1->left->right->left = NewNode(7);
	root_1->left->right->right = NewNode(8);
	printf("inorder_traversal:");
	inorder_traverse(root_1);
	printf("\n************\n");
	printf("Lowest Most Nodes with %d leaves: ",k);
	FindLowestNodesWithKleaves(root_1, k+1);
	printf("\n************\n");

	// // create tree 2
	struct Node* tree2_node_1 = NewNode(1);
	struct Node* root_2 = tree2_node_1;
	root_2->left = NewNode(3);
	root_2->left->right = NewNode(6);
	root_2->right = NewNode(2);
	root_2->right->left = NewNode(4);
	root_2->right->right = NewNode(5);
	root_2->right->right->left = NewNode(8);
	root_2->right->right->right = NewNode(7);
	printf("inorder_traversal:");
	inorder_traverse(root_2);
	printf("\n************\n");
	printf("Lowest Most Nodes with %d leaves: ",k);
	FindLowestNodesWithKleaves(root_2, k);
	printf("\n************\n");

}