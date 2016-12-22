#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* next;
};


struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data =data;
	new_node->next = NULL;
	return new_node;
}

void PrintLL(struct Node* head){
	if(head == NULL)
		return;
	printf("%d ", head->data);
	PrintLL(head->next);
}


struct Node* swap(struct Node* head, int k){
	int count =0;
	// either no elements or only one element exists
	// if(head==NULL || head->next == NULL)
	// 	return *head;
	struct Node* prev = NULL;
	struct Node* current = head;
	struct Node* next = NULL;
	while(current!=NULL && count<k){
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
		count++;
	}
	if(next!=NULL){
		head->next = swap(next, k);
	}
	return prev;
}

void InsertAnyWhere(struct Node** head, int data){
	struct Node* new_node = NewNode(data);
	struct Node* temp = *head;
	if(temp == NULL)
		*head = new_node;
	else{
		while(temp->next!=NULL)
			temp = temp->next;
		temp->next = new_node;
	}
}


int main(){
	struct Node* head =  NULL;
	InsertAnyWhere(&head, 1);
	InsertAnyWhere(&head, 2);
	InsertAnyWhere(&head, 3);
	InsertAnyWhere(&head, 4);
	InsertAnyWhere(&head, 5);
	PrintLL(head);
	printf("\n");
	head = swap(head, 2);
	PrintLL(head);
}