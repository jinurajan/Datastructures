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


int sum(struct Node* root){
	if(root == NULL)
		return 0;
	return sum(root->left)+root->data+sum(root->right);

}

int IsSumTree(struct Node* root){
	if(sum(root->left)+sum(root->right) == root->data)
		return 1;
	else
		return 0;

}


int main(){
// create tree 1
	struct Node* node_1 = NewNode(26);
	struct Node* root = node_1;
	root->left = NewNode(10);
	root->left->left = NewNode(4);
	root->left->right = NewNode(6);
	root->right = NewNode(3);
	root->right->right = NewNode(3);
	printf("%d\n", IsSumTree(root));

}