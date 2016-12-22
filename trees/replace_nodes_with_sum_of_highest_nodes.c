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

int sum_of_higher_values(struct Node* root){
	// considering leaf nodes will be replaced by 0
	// since there is no child to it
	if(root == NULL)
		return 0;
	return root->data+sum_of_higher_values(root->right);
}



void ReplaceNodes_method_2(struct Node* root){
	if(root ==NULL)
		return;
	if(root->right != NULL){
		// its a leaf node
		root->data = sum_of_higher_values(root->right);
	}
	ReplaceNodes_method_2(root->left);
	ReplaceNodes_method_2(root->right);
}

void ReplaceNodes(struct Node* root){
	if(root ==NULL)
		return;
	root->data = sum_of_higher_values(root->right);
	ReplaceNodes(root->left);
	ReplaceNodes(root->right);
}


void TestReplaceNodesMethod2(){
	struct Node* node_1 = NewNode(26);
	struct Node* root = node_1;
	root->left = NewNode(10);
	root->left->left = NewNode(4);
	root->left->right = NewNode(11);
	root->right = NewNode(30);
	root->right->right = NewNode(40);
	printf("\nTesting Method 2 with leaf nodes replaced as its own value\n");
	inorder_traverse(root);
	printf("\n");
	// method 2: leaf nodes will be returned as the same node value
	ReplaceNodes_method_2(root);
	inorder_traverse(root);
	printf("\n");
}


int main(){
// create tree 1
	/*
		  26
		/	\
	  10    30
	  / \	 \
	 4	 11    40
	*/
	struct Node* node_1 = NewNode(26);
	struct Node* root = node_1;
	root->left = NewNode(10);
	root->left->left = NewNode(4);
	root->left->right = NewNode(11);
	root->right = NewNode(30);
	root->right->right = NewNode(40);
	inorder_traverse(root);
	ReplaceNodes(root);
	printf("\n");
	inorder_traverse(root);
	TestReplaceNodesMethod2();
}