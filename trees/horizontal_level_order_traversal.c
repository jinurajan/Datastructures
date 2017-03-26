#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node* left;
	struct Node* right;
};


struct Node* NewNode(int data){
	struct Node* new_node  =(struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->right = NULL;
	new_node->left = NULL;
	return new_node;
}


int Height(struct Node* node){
	if(node == NULL)
		return 0;
	int lheight = Height(node->left);
	int rheight = Height(node->right);
	return lheight > rheight?lheight+1:rheight+1;
}

void PrintGivenLevel(struct Node* node, int level){

	if(node==NULL)
		return;
	if(level == 1)
		printf("%d ", node->data);
	PrintGivenLevel(node->left, level-1);
	PrintGivenLevel(node->right, level-1);
}


void PrintLevelOrder(struct Node* root){
	int height = Height(root);
	for(int i=1;i<=height;i++)
		PrintGivenLevel(root, i);
}


void InorderTraversal(struct Node* node){
	if(node==NULL){
		return;
	}
	InorderTraversal(node->left);
	printf("%d  ", node->data);
	InorderTraversal(node->right);
}


int main(){
	struct Node* root = NULL;
	root = NewNode(4);
	root->left = NewNode(2);
	root->left->right = NewNode(3);
	root->left->left = NewNode(1);
	root->right = NewNode(6);
	root->right->left = NewNode(5);
	PrintLevelOrder(root);

	struct Node* root_1 = NULL;
	root_1 = NewNode(1);
	root_1->right = NewNode(4);
	root_1->left = NewNode(2);
	root_1->left->left = NewNode(8);
	root_1->left->right = NewNode(5);
	root_1->left->right->right = NewNode(9);
	root_1->left->right->left = NewNode(10);
	printf("\n");
	PrintLevelOrder(root_1);

}