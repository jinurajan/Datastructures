#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* link;
};


struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->link = NULL;
	return new_node;
}


void PrintLL(struct Node* head){
	if(head == NULL)
		return;
	printf("%d ", head->data);
	PrintLL(head->link);
}


int GetLength(struct Node* head){
	if(head ==NULL)
		return 0;
	return 1+GetLength(head->link);
}

struct Node* InsertNode(struct Node* head, int data){
	struct Node* new_node = NewNode(data);
	struct Node* temp = head;
	if(head == NULL)
		head = new_node;
	while(temp->link!= NULL)
		temp = temp->link;
	temp->link = new_node;
	return head;
}


struct Node* Sum(struct Node* head, int array[], int n){
	int result_ll_size, i=0;
	int lheight = GetLength(head);
	if(n >=lheight)
		result_ll_size = n;
	else
		result_ll_size = lheight;

	struct Node* temp = head;
	struct Node* result_head = NULL;
	while(i<result_ll_size || temp !=NULL){
		printf(" head data: %d array: %d\n", temp->data, array[i]);
		struct Node* new_node = NewNode(temp->data+array[i]);
		if(i ==0)
			result_head = new_node;

		temp = temp->link;
		i = i+1;
	}
	return result_head;
}


int main(){

	// int array[] = {1,2,3};
	// int  n = sizeof(array)/sizeof(array[0]);
	// struct Node* new_node =  NewNode(1);
	// struct Node* head = new_node;
	// new_node->link = NewNode(2);
	// new_node->link->link = NewNode(3);

	// create another linked list L1 with root1
	struct Node* head1 = NULL;
	head1 = InsertNode(head1, 1);
	// InsertNode(head1, 2);
	// InsertNode(head1, 3);
	// InsertNode(head1, 4);
	// InsertNode(head1, 5);
	PrintLL(head1);
}