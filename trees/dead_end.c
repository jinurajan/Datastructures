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


void InorderTraversal(struct Node* node){
	if(node==NULL){
		return;
	}
	InorderTraversal(node->left);
	printf("%d  ", node->data);
	InorderTraversal(node->right);
}


int* Findleaves(struct Node * node, int** array, int n){
	if(node== NULL)
		return *array;
	if(node->left==NULL && node->right == NULL){
		// printf("%d is leaf node\n", node->data);
		*array[n] = node->data;
		n = n+1;
		return *array;
	}
	Findleaves(node->left,array, n);
	Findleaves(node->right, array, n);
}


struct Node* Insert(struct Node* node, int data){ 
	if(node==NULL)
		return NewNode(data);
	if(data < node->data)
		node->left = Insert(node->left, data);
	else if (data > node->data)
		node->right = Insert(node->right, data);
	return node;
}


int main(){
	struct Node* root = NULL;
	root = Insert(root, 4);
	Insert(root, 2);
	Insert(root, 3);
	Insert(root, 1);
	Insert(root, 6);
	Insert(root, 5);
	InorderTraversal(root);
	printf("\n");
	int array[10]; 
	Findleaves(root,&array, 0);
	for(int i=0;i<10;i++)
		printf("%d\n", array[i]);

}