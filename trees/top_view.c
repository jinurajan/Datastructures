#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

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

void PrintGivenVerticalLevel(struct Node* root, int line_number, int horizontal_distance, int* visited, int max)
{
	if(root==NULL)
		return;
	if(horizontal_distance == line_number){
		visited[horizontal_distance+max-1] = root->data;
	}
	else{
		PrintGivenVerticalLevel(root->left, line_number, horizontal_distance-1, visited, max);
		PrintGivenVerticalLevel(root->right, line_number, horizontal_distance+1, visited, max);
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


void TopView(struct Node* root){
	int min, max;
	FindMinMax(root, &min, &max, 0);
	int visited_array_length = max+(-min)+1;
	int visited[visited_array_length];
	for(int j=0;j<visited_array_length;j++)
		visited[j] = 0;
	for(int i=min; i <=max;i++){
		PrintGivenVerticalLevel(root, i, 0, visited, max);
	}
	for(int i=0;i<visited_array_length;i++)
		printf("%d ", visited[i]);
}

int main(){
	// struct Node* root = NULL;
	// root = NewNode(4);
	// root->left = NewNode(2);
	// root->left->right = NewNode(3);
	// root->left->left = NewNode(1);
	// root->right = NewNode(6);
	// root->right->left = NewNode(5);
	// InorderTraversal(root);
	// printf("\n");
	// TopView(root);

	// struct Node* root_1 = NULL;
	// root_1 = NewNode(1);
	// root_1->right = NewNode(4);
	// root_1->left = NewNode(2);
	// root_1->left->left = NewNode(8);
	// root_1->left->right = NewNode(5);
	// root_1->left->right->right = NewNode(9);
	// root_1->left->right->left = NewNode(10);
	// printf("\n");
	// TopView(root_1);

	// struct Node* root_2 = NULL;
	// root_2 = NewNode(1);
	// root_2->left = NewNode(2);
	// root_2->left->left = NewNode(4);
	// root_2->left->right = NewNode(5);
	// root_2->right = NewNode(3);
	// root_2->right->right = NewNode(7);
	// root_2->right->left = NewNode(6);
	// printf("\n");
	// TopView(root_2);


	struct Node* root_3 = NewNode(1);
	root_3->right = NewNode(3);
	root_3->left = NewNode(2);
	root_3->left->right = NewNode(4);
	root_3->left->right->right = NewNode(5);
	root_3->left->right->right->right = NewNode(6);
	printf("\n");
	TopView(root_3);


}