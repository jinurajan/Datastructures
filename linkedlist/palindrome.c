// Author: Jinu.P.R
// Date: Dec 22 2016
// Copyright: Always restricted to those who know what linkedlist is and how does it work ;)
// http://www.practice.geeksforgeeks.org/problem-page.php?pid=700391

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

/* 
	Method 1:
	Use a stack to store the values
	pop from stack and compare with current element if same proceed
	else break
*/


void TestPalindrome(){
	struct Node* head = NULL;
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	AppendIteration(&head, 2);
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	struct Node* top = push(head, NULL)
	// return IsPalindrome(head);
}

int main(){
	TestPalindrome();
}


