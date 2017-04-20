#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
	int data;
	struct Node* next;
	struct Node* prev;
}Node;

// create a node with given integer
Node* NewNode(int data){
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data;
	new_node->next = NULL;
	new_node->prev = NULL;
	return new_node;
}



//   print a linkedlist given the head node
void PrintLList(Node* node){
	while(node!=NULL){
		printf("%d ", node->data);
		node = node->next;
	}
}



Node* SortedInsert(Node *head,int data){
	Node* current = head;
	Node* prev=NULL;
	if(current==NULL){
		head = NewNode(data);
	}
	else if(current->data > data){
		// in the beginning as head node
		head = NewNode(data);
		head->next = current;
		current->prev = head;
	}
	else{
		//  it can be in the middle or at the end
		// if at end current will be NULL and prev number will be the last element
		while(current && data > current->data){
			prev = current;
			current = current->next;
		}

		Node* temp = NewNode(data);
		prev->next = temp;
		temp->prev = prev;
		if(current){
			temp->next = current;
			current->prev = temp;	
		}
		
	}
	return head;
}

int main(){
	Node* head = NULL;
	head = SortedInsert(head, 3);
	PrintLList(head);
	printf("\n");
	head = SortedInsert(head, 1);
	PrintLList(head);
	printf("\n");
	head = SortedInsert(head, 2);
	PrintLList(head);
	printf("\n");
	head = SortedInsert(head, 4);
	PrintLList(head);
}