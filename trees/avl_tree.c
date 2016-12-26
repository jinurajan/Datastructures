#include<stdio.h>
#include<stdlib.h>


struct Node{
	int data;
	int height;
	struct Node* left;
	struct Node* right;
};

struct Node* NewNode(int data){
	struct Node* new_node =(struct Node*)malloc(sizeof(struct Node));
	new_node->data= data;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->height = 1;
	return new_node;
}

int height(struct Node* node){
	if(node==NULL)
		return 0;
	return node->height;
}

int balance_factor(struct Node* node){
	if(node==NULL)
		return 0;
	return height(node->left) - height(node->right);
}

int max(int a, int b){
	return (a > b)? a : b;
}

void inorder_traverse(struct Node* root){
	if(root == NULL)
		return;
	inorder_traverse(root->left);
	printf("%d ", root->data);
	inorder_traverse(root->right);
}

struct Node* right_rotate(struct Node* y){
	struct Node* x = y->left;
	struct Node* T2 = x->right;
	x->right = y;
	y->left = T2;

	// update the heights	
	x->height = 1+max(height(x->left), height(x->right));
	y->height = 1+max(height(y->left), height(y->right));

	return x;
}


struct Node* left_rotate(struct Node* x){
	struct Node* y = x->right;
	struct Node* T1 = y->left;
	y->left = x;
	x->right = T1;
	// update the heights
	x->height = 1+max(height(x->left), height(x->right));
	y->height = 1+max(height(y->left), height(y->right));
	return y;
}


struct Node* Insert(struct Node* node, int data){ 
	if(node==NULL)
		return NewNode(data);
	if(data < node->data){
		node->left = Insert(node->left, data);
	}
	else if (data > node->data){
		node->right = Insert(node->right, data);
	}
	else
		return node;
	// update the heights
	node->height = 1+max(height(node->left), height(node->right));

	int bf = balance_factor(node);
	if(bf >1 && data < node->left->data){
		// left left case
		return right_rotate(node);
	}
	if(bf < -1 && data > node->right->data){
		// right right case
		return left_rotate(node);
	}
	if(bf >1 && data > node->left->data){
		// left right case
		node->left = left_rotate(node->left);
		return right_rotate(node);
	}
	if(bf < -1 && data < node->right->data){
		// right left case
		node->right = right_rotate(node->right);
		return left_rotate(node);
	}
	return node;

}

int main(){
	struct Node* root = NULL;
	root = Insert(root, 4);
	root = Insert(root, 2);
	root = Insert(root, 3);
	root = Insert(root, 1);
	root = Insert(root, 6);
	root = Insert(root, 5);
	root = Insert(root, 7);
	root = Insert(root, 8);
	inorder_traverse(root);
	// printf("%d\n", height(root));

}


