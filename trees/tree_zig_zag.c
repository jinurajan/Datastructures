#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};

struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data =data;
	new_node->left = NULL;
	new_node->right = NULL;
	return new_node;
}


int GetHeight(struct Node* root){
	if(root == NULL)
		return 0;
	else{
		int lheight = GetHeight(root->left);
		int rheight = GetHeight(root->right);
		if(lheight>rheight)
			return lheight+1;
		else
			return rheight+1;
	}
}

void PrintGivenLevel(struct Node* root, int level, int flag){
	if(root==NULL)
		return;
	if(level == 1)
		printf("%d ", root->data);
	else if (level>1){
		if(flag){
			PrintGivenLevel(root->left, level-1, flag);
			PrintGivenLevel(root->right, level-1, flag);
		}
		else
		{
			PrintGivenLevel(root->right, level-1, flag);
			PrintGivenLevel(root->left, level-1, flag);
		}
	}
}

void ZigZagTraversal(struct Node* root){
	int height = GetHeight(root);
	int flag = 0;
	for(int i=1; i<=height;i++){
		PrintGivenLevel(root, i, flag);
		if(flag==1)
			flag = 0;
		else
			flag = 1;
	}

}

void LeftToRightTraversal(struct Node* root){
	int height = GetHeight(root);
	int flag = 1;
	for(int i=1; i<=height;i++){
		PrintGivenLevel(root, i, flag);
	}
}

void RightToLeftTraversal(struct Node* root){
	int height = GetHeight(root);
	int flag = 0;
	for(int i=1; i<=height;i++){
		PrintGivenLevel(root, i, flag);
	}
}



int main(){
	struct Node* root = NewNode(1);
	root->left = NewNode(2);
	root->right = NewNode(3);
	root->left->left = NewNode(7);
	root->left->right = NewNode(6);
	root->right->right = NewNode(4);
	root->right->left = NewNode(5);
	PrintGivenLevel(root, 3, 1);
	// ZigZagTraversal(root);
	// printf("\n");
	// LeftToRightTraversal(root);
	// printf("\n");
	// RightToLeftTraversal(root);

}