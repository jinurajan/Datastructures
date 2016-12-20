#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};


int sum(struct Node* root){
	if(root == NULL)
		return 0;
	return sum(root->left) + root->data + sum(root->right);
}


void IsSumTree(struct Node* root_1){

	if(sum(root_1->left)+sum(root_1->right) == root_1->data)
		printf("This is a sum Tree\n");
	else
		printf("This is not a sum Tree\n");
}


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

void preorder_traversal(struct Node* root){
	if(root ==NULL)
		return;
	printf("%d ", root->data);
	preorder_traversal(root->left);
	preorder_traversal(root->right);

}

void postorder_traversal(struct Node* root){

	if(root ==NULL)
		return;
	postorder_traversal(root->left);
	postorder_traversal(root->right);
	printf("%d ", root->data);
}



int main(){

	struct Node* new_node_1 = NewNode(4);
	struct Node* root = new_node_1;
	root->left = NewNode(3);
	root->right = NewNode(5);
	root->left->left = NewNode(2);
	root->left->left->left = NewNode(1);
	root->right->left = NewNode(6);
	root->right->right = NewNode(7);


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
	// inorder_traverse(root_2);
	// printf("\n************\n");

	IsSumTree(root_1);
	IsSumTree(root_2);
	IsSumTree(root);

}