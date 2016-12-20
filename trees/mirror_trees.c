#include<stdio.h>
#include<stdlib.h>


struct Node {
	int data;
	struct Node* left;
	struct Node* right;
};


struct Node* NewNode(int data){

	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->left = NULL;
	new_node->right = NULL;
	return new_node;
}


void inorder_traversal(struct Node* node){
	if(node == NULL)
		return;
	inorder_traversal(node->left);
	printf("%d\t", node->data);
	inorder_traversal(node->right);
}



int isMirror(struct Node* root_1, struct Node* root_2){
	if(root_1==NULL && root_2==NULL)
		return 1;
	if(root_1 == NULL || root_2 == NULL)
		return 0;
	return (root_1->data == root_2->data)&& isMirror(root_1->left, root_2->right) && isMirror(root_1->right, root_2->left);
}



int main(){


	//create tree 1
	struct Node* node_1 = NewNode(1);
	struct Node* root_1 = node_1;
	root_1->left = NewNode(3);
	root_1->right = NewNode(2);
	root_1->right->right = NewNode(4);
	root_1->right->left = NewNode(5);
	// inorder_traversal(root_1);
	// printf("\n");

	//create tree 2
	struct Node* node_2 = NewNode(1);
	struct Node* root_2 = node_2;
	node_2->right = NewNode(3);
	node_2->left = NewNode(2);
	node_2->left->left = NewNode(4);
	node_2->left->right = NewNode(5);
	// inorder_traversal(root_2);
	int result = isMirror(root_1, root_2);
	printf("%d\n", result);



}