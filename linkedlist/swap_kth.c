#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* next;
};


void printList(struct Node* n){
	while (n!=NULL){
		printf("%d   ",n->data);
		n = n->next;
	}
}

int count_nodes(struct Node* head){
	int count = 0;
	struct Node* temp = head;
	while(temp!= NULL){
		count = count+1;
		temp = temp->next;
	}
	return count;
}

void insert(struct Node** head,int data){
	struct Node* temp = *head;
	struct Node* new_node =  (struct Node *) malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->next = NULL;
	if (*head == NULL){
		*head = new_node;
		return;
	}
	while(temp->next!=NULL)
		temp= temp->next;
	temp->next = new_node;
	return;

}

int main(){
	struct Node* head = NULL;
	insert(&head, 1);
	insert(&head, 2);
	insert(&head, 3);
	insert(&head, 4);
	insert(&head, 5);
	printList(head);
	printf("\n*************\n");
	swap_kth_elements(&head, 2);
	printList(head);

}