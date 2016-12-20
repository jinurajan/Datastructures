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


int Search(struct Node* node, int key){
	if(node==NULL)
		return 0;
	if(node->data == key)
		return 1;
	if(key > node->data)
		return Search(node->right, key);
	else if(key < node->data)
		return Search(node->left, key);
	return 0;
}


struct Node* SearchForNode(struct Node* node, int key){
	if(node==NULL || node->left->data==key || node->right->data==key)
		return node;
	if(key >node->data)
		return SearchForNode(node->right, key);
	return SearchForNode(node->left, key);
}

int GetNumberOfchilds(struct Node* node){
	if(node==NULL)
		return 0;
	if(node->left != NULL && node->right !=NULL)
		return 2;
	else if(node->left !=NULL || node->right!=NULL)
		return 1;
	else
		return 0;
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

struct Node* MinValueNode(struct Node* node){
	struct Node* current = node;
	while(current->left !=NULL)
		current = current->left;
	return current;
}


struct Node* Delete(struct Node* node, int data){
	if(node==NULL){
		return node;
	}
	if(node->data == data){
		free(node);
		return NULL;
	}
	if(data > node->data)
		node->right = Delete(node->right, data);
	else if(data < node->data)
		node->left = Delete(node->left, data);
	else{
		// one child or no child
		if(node->left ==NULL && node->right ==NULL){
			printf("node:%d has no child\n", );
		}
		else if(node->left==NULL && node->right!=NULL){
			struct Node* temp = node->right;
			free(node);
			return temp;
		}
		else if(node->right ==NULL && node->left !=NULL){
			struct Node* temp = node->left;
			free(node);
			return temp;
		}
		// it has two childs
		struct Node* temp = MinValueNode(node->left);
		node->data = temp->data;
		node->left = Delete(node->left, temp->data);

	}
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
	// printf("\n%d\n",Search(root, 5));
	printf("\n");
	Delete(root, 1);
	InorderTraversal(root);
	printf("\n");
	Delete(root, 6);
	InorderTraversal(root);
	printf("\n");
	Delete(root, 3);
	InorderTraversal(root);
	printf("\n");
	Delete(root, 4);
	InorderTraversal(root);
	// printf("\n");
	// Delete(root, 5);
	// InorderTraversal(root);
	// printf("\n");
	// Delete(root, 2);
	// Insert(root, 5);
	// InorderTraversal(root);
	// printf("\n");

}