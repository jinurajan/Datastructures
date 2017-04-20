// Reverse a doubly linked list
#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
 int data;
 struct Node* next;
 struct Node* prev;
} Node;


Node* NewNode(int data){
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data;
	new_node->prev = NULL;
	new_node->next = NULL;
	return new_node;
}


void PrintLL(Node* head){
	while(head !=NULL){
		printf("%d ", head->data);
		head = head->next;
	}
}


Node* Reverse(Node* head){
	// use 3 pointers



}



void ReverseRecursion(Node** head){
	Node* first;
	Node* rest;
	if((*head) == NULL)
		return;
	first = (*head);
	rest = first->next;
	if(rest ==NULL){
		// when there is only one element
		return;
	}
	ReverseRecursion(&rest);
	first->next->next = first;
	first->next->prev = rest->next;
	first->next = NULL;
	first->prev = rest;
	(*head) = rest;
}


int main(){
	Node* head1 = NULL;
	// base cases
	ReverseRecursion(&head1);
	PrintLL(head1);
	head1 = NewNode(2);
	Node* temp = NewNode(3);
	head1->next = temp;
	temp->prev = head1;
	printf("original: ");
	PrintLL(head1);
	ReverseRecursion(&head1);
	printf("\nAfter reversing:");
	PrintLL(head1);
	printf("\n");
	Node* temp1 = NewNode(4);
	head1->next->next = temp1;
	temp1->prev = head1->next;
	printf("original: ");
	PrintLL(head1);
	ReverseRecursion(&head1);
	printf("\nAfter reversing:");
	PrintLL(head1);
	printf("\n");
}