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


int HorizontalDistance(struct Node* root){
	if(root == NULL)
		return 0;
	else{
		int lheight = HorizontalDistance(root->left);
		int rheight = HorizontalDistance(root->right);
		if(lheight>rheight)
			return lheight-1;
		else
			return rheight+1;
	}
}

void FindMinMax(struct Node* root, int* min, int* max, int hd){
	if(root==NULL)
		return;
	if(hd < *min)
		*min = hd;
	else if(hd > *max)
		*max = hd;
	FindMinMax(root->left, min, max, hd-1);
	FindMinMax(root->right, min, max, hd+1);
}

void PrintGivenVerticalLevel(struct Node* root, int line_number, int horizontal_distance){
	if(root==NULL)
		return;
	if(horizontal_distance == line_number)
		printf("%d ", root->data);
	PrintGivenVerticalLevel(root->left, line_number, horizontal_distance-1);
	PrintGivenVerticalLevel(root->right, line_number, horizontal_distance+1);
}


void InorderTraversal(struct Node* node){
	if(node==NULL){
		return;
	}
	InorderTraversal(node->left);
	printf("%d  ", node->data);
	InorderTraversal(node->right);
}


void HorizontalTraversal(struct Node* root){
	int min, max;
	FindMinMax(root, &min, &max, 0);
	for(int i=min; i <=max;i++)
		PrintGivenVerticalLevel(root, i, 0);
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
	HorizontalTraversal(root);

	struct Node* root_1 = NULL;
	root_1 = NewNode(1);
	root_1->right = NewNode(4);
	root_1->left = NewNode(2);
	root_1->left->left = NewNode(8);
	root_1->left->right = NewNode(5);
	root_1->left->right->right = NewNode(9);
	root_1->left->right->left = NewNode(10);
	printf("\n");
	HorizontalTraversal(root_1);

}