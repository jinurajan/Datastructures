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


int Height(struct Node* root){
	if(root == NULL)
		return 0;
	else{
		int lheight = Height(root->left);
		int rheight = Height(root->right);
		if(lheight>rheight)
			return lheight+1;
		else
			return rheight+1;
	}
}

void PrintGivenLevel(struct Node* root, int level){
	if(root==NULL)
		return;
	if(level == 1)
		printf("%d ", root->data);
	else if (level>1){
		PrintGivenLevel(root->left, level-1);
		PrintGivenLevel(root->right, level-1);
	}
}

void PrintGivenLevelFromRight(struct Node* root, int level){
	if(root==NULL)
		return;
	if(level == 1)
		printf("%d ", root->data);
	else if (level>1){
		PrintGivenLevelFromRight(root->right, level-1);
		PrintGivenLevelFromRight(root->left, level-1);
	}
}

void InorderTraversal(struct Node* node){
	if(node==NULL){
		return;
	}
	InorderTraversal(node->left);
	printf("%d  ", node->data);
	InorderTraversal(node->right);
}


void LevelOrderTraversal(struct Node* root){
	int height = Height(root);
	for(int i=0; i<=height;i++)
		PrintGivenLevel(root, i);
}

void LevelOrderTraversalFromRight(struct Node* root){
	int height = Height(root);
	for(int i=0; i<=height;i++)
		PrintGivenLevelFromRight(root, i);
}

int main(){
	struct Node* root = NULL;
	root = NewNode(4);
	root->left = NewNode(2);
	root->left->right = NewNode(3);
	root->left->left = NewNode(1);
	root->right = NewNode(6);
	root->right->left = NewNode(5);
	InorderTraversal(root);
	printf("\n");
	LevelOrderTraversal(root);
	printf("\n");
	LevelOrderTraversalFromRight(root);

	struct Node* root_1 = NULL;
	root_1 = NewNode(1);
	root_1->right = NewNode(4);
	root_1->left = NewNode(2);
	root_1->left->left = NewNode(8);
	root_1->left->right = NewNode(5);
	root_1->left->right->right = NewNode(9);
	root_1->left->right->left = NewNode(10);
	printf("\n");
	InorderTraversal(root_1);
	printf("\n");
	LevelOrderTraversal(root_1);
	printf("\n");
	LevelOrderTraversalFromRight(root_1);

}