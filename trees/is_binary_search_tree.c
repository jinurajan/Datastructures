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


// Time Complexity: O(n)

int IsBSTUtil(struct Node* node, int min, int max){
	if(node==NULL)
		return 1;
	if(node->data < min || node->data > max)
		return 0;
	return IsBSTUtil(node->left, min,  node->data+1) &&
		   IsBSTUtil(node->right, node->data-1, max);

}


int IsBST(struct Node* root){
	return IsBSTUtil(root, INT_MIN, INT_MAX);
}


int IsBSTUtil_1(struct Node* node, int min, int max){
	if(node==NULL)
		return 1;
	if(node->data <= min || node->data >= max)
		return 0;
	return IsBSTUtil(node->left, min,  node->data) &&
		   IsBSTUtil(node->right, node->data, max);

}

int IsBST_1(struct Node* root){
	return IsBSTUtil_1(root, INT_MIN, INT_MAX);
}



int main(){

	struct Node* new_node_1 = NewNode(4);
	struct Node* root = new_node_1;
	root->left = NewNode(3);
	root->right = NewNode(6);
	root->left->left = NewNode(2);
	root->left->left->left = NewNode(1);
	root->right->left = NewNode(5);
	root->right->right = NewNode(7);
	inorder_traverse(root);
	printf("\n************\n");
	printf("%d\n", IsBST(root));
	printf("\n************\n");
	printf("%d\n", IsBST_1(root));
	


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
	printf("%d\n", IsBST(root_1));
	printf("\n************\n");
	printf("%d\n", IsBST_1(root_1));
	
	

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
	printf("\n************\n");
	printf("%d\n", IsBST(root_2));
	printf("\n************\n");
	printf("%d\n", IsBST_1(root_2));
	
	

}