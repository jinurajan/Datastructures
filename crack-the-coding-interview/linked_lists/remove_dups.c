/*
	Remove Dups! Write code to remove duplicates from an unsorted linked list.
	FOLLOW UP
	How would you solve this problem if a temporary bu er is not allowed?
*/


#include<stdio.h>
#include<stdlib.h>


struct Node{
	int data;
	struct Node* next;
};



struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->next = NULL;
	return new_node;
}


void printLL(struct Node* head){
	struct Node* p = head;
	while(p->next != NULL){
		printf("%d ", p->data);
		p = p->next;
	}
}



struct Node* removeDups(struct Node* head){
	// brute force algorithm.compare each node with rest of it
	struct Node* current = head;
	struct Node* next = head;

	if current == NULL || current->next == NULL{
		// empty or single linkedlist node
		return head;
	}
	next = current->next;
	while(current->data != next->data){
		next = current->next;
		if(next == NULL){
			// reached end of the LL
			next = current->next;
			current = current->next;
		}
	}


}


int main(){
	struct Node* head = NewNode(1);
	head->next = NewNode(2);
	head->next->next = NewNode(2);
	head->next->next->next = NewNode(3);
	head->next->next->next->next = NewNode(3);

	printLL(head);
}


