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

int Length(struct Node* head){
	if(head == NULL)
		return 0;
	return 1+Length(head->next);
}


void PrintLL(struct Node* head){
	if(head == NULL)
		return;
	printf("%d ", head->data);
	PrintLL(head->next);
}

void InsertAtFront(struct Node** head, int data){
	struct Node* new_node = NewNode(data);
	new_node->next = *head;
	*head = new_node;
}

void InsertAtEnd(struct Node** head, int data){
	struct Node* new_node = NewNode(data);
	struct Node* temp = *head;
	while(temp->next !=NULL)
		temp = temp->next;
	temp->next = new_node;
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

void InsertAtIndex(struct Node** head, int data, int index){
	struct Node* temp = *head;
	int i = 0;
	printf("length: %d index: %d\n", Length(*head), index);
	int length = Length(*head);
	if(index+1 >length){
		printf("Cannot Insert data:%d At Index:%d\n", data, index);
		return;
	}
	if(index == length)
		InsertAtEnd(head, data);
	if(index==0)
		InsertAtFront(head, data);
	else{
		while(index-1>i){
			temp = temp->next;
			i+=1;
		}
		struct Node* new_node = NewNode(data);
		new_node->next = temp->next;
		temp->next = new_node;
	}
}

void DeleteAtFront(struct Node** head){
	if(*head == NULL)
		return;
	struct Node* temp =  *(head);
	free(*head);
	*head  = temp->next;
}

void DeleteAtEnd(struct Node** head){
	struct Node* temp = *head;
	while(temp->next->next != NULL)
		temp = temp->next;
	free(temp->next);
	temp->next = NULL;
}

void DeleteAtIndex(struct Node** head, int index){
	int length = Length(*head);
	if(index == 0)
		DeleteAtFront(head);
	if(index == length)
		DeleteAtEnd(head);
	else{
		struct Node* temp = *head;
		struct Node* prev = NULL;
		int i = 0;
		while(i<length){
			prev = temp;
			temp = temp->next;
			i++;
		}
		prev->next = temp->next;
		free(temp);
	}
}


int main(){
	struct Node* head =  NULL;
	InsertAtFront(&head, 1);
	printf("Inserted element:%d at front: ",1);
	PrintLL(head);
	InsertAtEnd(&head,2);
	InsertAtEnd(&head,3);
	InsertAtEnd(&head,4);
	printf("\nInserted 3 elements at end: ");
	PrintLL(head);
	InsertAnyWhere(&head, 5);
	printf("\nInserted one more element at the end: ");
	PrintLL(head);
	InsertAtIndex(&head, 5, 2);
	printf("\nInserted key:%d at index:%d  and tree is: ",5,2);
	PrintLL(head);
	InsertAtIndex(&head, 7, 0);
	printf("\nInserted key:%d at index:%d  and tree is: ",7,0);
	PrintLL(head);
	InsertAtIndex(&head, 0, 7);
	printf("\nInserted key:%d at index:%d  and tree is: ",0,7);
	PrintLL(head);
	InsertAtIndex(&head, 1, 9);
	printf("Final Linked List is: ");
	PrintLL(head);
	printf("\n");
	DeleteAtFront(&head);
	PrintLL(head);
	printf("\n");
	DeleteAtEnd(&head);
	PrintLL(head);
	printf("\n");
	DeleteAtIndex(&head, 5);
	PrintLL(head);
	DeleteAtIndex(&head, 0);
	PrintLL(head);
}