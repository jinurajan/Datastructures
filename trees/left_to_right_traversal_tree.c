/*left to right traversal*/


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

int height(struct Node* node){
	if(node==NULL)
		return 0;
	else{
		int ldepth = height(node->left);
		int rdepth = height(node->right);
		if(ldepth > rdepth)
			return ldepth+1;
		else
			return rdepth+1;
	}
}

void PrintGivenLevel(struct Node* node, int level){
	if(node == NULL)
		return;
	if(level == 1){
		printf("%d ", node->data);
	}
	else{
		PrintGivenLevel(node->left, level-1);
		PrintGivenLevel(node->right, level-1);
	}
}


void LeftToRightTraversal(struct Node* root){
	int h = height(root);
	for(int i=1; i<=h;i++){
		PrintGivenLevel(root, i);
	}
}

/*
		5
	3		7
1	  4   6   8

*/




int main(){
	struct Node* root = NewNode(5);
	root->left = NewNode(3);
	root->left->right = NewNode(4);
	root->left->left = NewNode(1);
	root->right = NewNode(7);
	root->right->left = NewNode(6);
	root->right->right = NewNode(8);
	LeftToRightTraversal(root);
}