// Author: Jinu.P.R
// Date: Dec 5 2016
// Copyright: Always restricted to those who know what linkedlist is and how does it work ;)


#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node* next;
};


// create a node with given integer
struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->next = NULL;
	return new_node;
}

//  print a linkedlist given the head node
void PrintLList(struct Node* node){
	while(node!=NULL){
		printf("%d ", node->data);
		node = node->next;
	}
}

/********************************Deletion Methods***************************************/

void DeleteIteration(struct Node** head, int data){
	struct Node* temp = *head;
	struct Node* prev = NULL;
	if(temp->data == data){
		// Node to delete is the head node
		*head = temp->next;
		free(temp);
		return;
	}
	while(temp->data != data && temp->next!=NULL){
		prev =temp;
		temp = temp->next;
	}
	if(temp->data != data || temp ==NULL){
		printf("Data:%d does not exists\n", data);
		return;
	}
	prev->next = temp->next;
	free(temp);
	return;
}


/********************************Insertion Methods***************************************/

// append using iteration method
void AppendIteration(struct Node** head, int data){
	struct Node* new_node = NewNode(data);
	if(*head==NULL){
		*(head) = new_node;
		return;
	}
	struct Node* temp = *(head);
	while(temp->next != NULL)
		temp= temp->next;
	temp->next = new_node;
	return;
}

// append using recursion method
struct Node* AppendRecursion(struct Node* node, int data){
	if(node ==NULL){
		node = NewNode(data);
		return node;
	}
	node->next = AppendRecursion(node->next, data);
	return node;
}

// append in the reverse

void Prepend(struct Node** head, int data){
	struct Node* temp;
	temp = NewNode(data);
	temp->next = *head;
	*head = temp;
}

/* insert at an index
	assumption: index starts at 0
*/

void InsertAtIndex(struct Node** head, int data, int index){
	if(index ==0 ||*head ==NULL){
		// insert at the beginning
		struct Node* temp = NewNode(data);
		temp->next = *head;
		*head = temp;
		return;
	}
	int i =0;
	struct Node* current = *head;
	struct Node* prev = NULL;
	while(i<index && current!=NULL){
		prev = current;
		current = current->next;
		i+=1;
	}
	if(i+1!=index){
		printf("Cannot insert:%d at index:%d\n", data, index);
		return;
	}
	struct Node* new_node = NewNode(data);
	prev->next = new_node;
	new_node->next = current;
	return;
}



/********************************Insertion Methods End***************************************/

/**************************************************Find Length of linkedlist***********************************************/

int LengthIterative(struct Node* node){
	struct Node* temp =node;
	int length = 0;
	while(temp!=NULL){
		temp = temp->next;
		length = length+1;
	}
	return length;
}


int LengthRecursive(struct Node* node){
	if(node == NULL)
		return 0;
	return 1+LengthRecursive(node->next);
}

/**************************************************Find Length of linkedlist***********************************************/


//  Testing AppendIteration Method
void TestAppendIteration(){
	struct Node* head = NULL;
	int n = 1;
	while(n<=5){
 		AppendIteration(&head, n);
 		n+= 1;
	}
 	PrintLList(head);
 	printf("\nAppendIteration tested successfully\n");
}


//  Testing AppendRecursion Method
void TestAppendRecursion(){
	struct Node* head = NULL;
	int n=1;
	while(n<=5){
		head = AppendRecursion(head, n);
		n+=1;
	}
	PrintLList(head);
	printf("\nAppendRecursion tested successfully\n");
}


void TestPrepend(){
	struct Node* head = NULL;
	int n=1;
	while(n<=5){
		Prepend(&head, n);
		n+= 1;
	}
	PrintLList(head);
	printf("\nPrepend tested successfully\n");
}


void TestInsertAtIndex(){
	struct Node* head = NULL;
	int n=1;
	// inserting in order
	while(n<=5){
		InsertAtIndex(&head, n, n-1);
		n+=1;
	}
	PrintLList(head);
	printf("\nInserting in order worked\n");
	// Insert in the Middle
	InsertAtIndex(&head, 6, 3);
	PrintLList(head);
	printf("\nInserting in the middle worked\n");
	// Insert in the Front
	InsertAtIndex(&head, 7, 0);
	PrintLList(head);
	printf("\nInserting at the front worked\n");
	// Insert at the End
	InsertAtIndex(&head, 8,7);
	PrintLList(head);
	printf("\nInserting at the end worked\n");
	// Insert at an index which does not exists
	InsertAtIndex(&head, 10,10);
	PrintLList(head);
	printf("\nInserting at an index greater than length of linkedlist worked\n");

}


void TestDeleteIteration(){
	// Create Linked list to Test with
	struct Node* head = NULL;
	int n=1;
	while(n<=5){
		head = AppendRecursion(head, n);
		n+=1;
	}
	printf("Testing Deleting Using Iteration. Below is the linkedlist\n");
	PrintLList(head);
	printf("\n");
	// Delete the head
	printf("Deleting element 1 from the above linked list\n");
	DeleteIteration(&head, 1);
	PrintLList(head);
	printf("\nDeleting the head node worked\n");
	DeleteIteration(&head, 5);
	PrintLList(head);
	printf("\nDeleting the tail node worked\n");
	DeleteIteration(&head, 3);
	PrintLList(head);
	printf("\nDeleting the Middle node worked\n");
	// FIXME: not working for nodes which does not exists
	DeleteIteration(&head, 10);
	PrintLList(head);
	printf("\nDeleting a Non existing node worked\n");

}



void TestLength(){
	// Create Linked list to Test with
	struct Node* head = NULL;
	int n=1;
	while(n<=5){
		head = AppendRecursion(head, n);
		n+=1;
	}
	printf("Testing Length Using Iteration. Below is the linkedlist\n");
	PrintLList(head);
	printf("\nLength of linkedlist using iteration is: %d", LengthIterative(head)); 
	printf("\nLength of linkedlist using recursion is: %d\n", LengthRecursive(head)); 

}


 int main(void){
 	TestAppendIteration();
 	TestAppendRecursion();
 	TestPrepend();
 	TestInsertAtIndex();
 	TestDeleteIteration();
 	TestLength();
 	return 0;
 }