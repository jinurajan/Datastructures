#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};


int IsIsomorphic(struct Node* n1, struct Node* n2){
	if (n1 == NULL && n2 == NULL)
		return 1;
	if(n1==NULL || n2 == NULL)
		return 0;
	if (n1->data != n2->data)
    	return 0;

	return (IsIsomorphic(n1->left, n2->left) && IsIsomorphic(n1->right, n2->right))||
	(IsIsomorphic(n1->left, n2->right) && IsIsomorphic(n1->right, n2->left));
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
	struct Node* new_node_1 = NULL;
	new_node_1 = NewNode(4);
	struct Node* root = new_node_1;
	root->left = NewNode(3);
	root->right = NewNode(5);
	root->left->left = NewNode(2);
	root->left->left->left = NewNode(1);
	root->right->left = NewNode(6);
	root->right->right = NewNode(7);
	printf("inorder_traversal:");
	inorder_traverse(root);
	printf("\npreorder_traversal:");
	preorder_traversal(root);
	printf("\npostorder_traversal:");
	postorder_traversal(root);
	printf("\n************\n");


	// create tree 1
	struct Node* tree1_node_1 = NewNode(1);
	struct Node* root_1 = tree1_node_1;
	root_1->left = NewNode(2);
	root_1->right = NewNode(3);
	root_1->right->left = NewNode(6);
	root_1->left->left = NewNode(4);
	root_1->left->right = NewNode(5);
	root_1->left->right->left = NewNode(7);
	root_1->left->right->right = NewNode(8);
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
	inorder_traverse(root_2);
	printf("\n************\n");

	int isomorphic = IsIsomorphic(root_1, root_2);
	if(isomorphic == 0)
		printf("Yes");
	else
		printf("No");

}