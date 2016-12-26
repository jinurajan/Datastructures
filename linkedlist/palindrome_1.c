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

int NthElement(struct Node* head, int n){
	int count=1;
	struct Node* temp = head;
	while(count<n && temp !=NULL){
		temp = temp->next;
		count+=1;
	}
	return temp->data;
}

int NthLastElement(struct Node*head, int n){
	int count=1;
	struct Node* ref = head;
	struct Node* main = head;
	while(count<n && ref !=NULL){
		ref = ref->next;
		count = count+1;
	}
	while(ref->next!=NULL){
		main= main->next;
		ref = ref->next;

	}
	return main->data;
}


int height(struct Node* node){
	if(node == NULL)
		return 0;
	return 1+height(node->next);
}

int IsPalindrome(struct Node* head){
	int h = height(head);
	if(h==0){
		printf("LL is empty\n");
		return 0;
	}
	if(h==1){
		return 1;
	}
	int result = 0;
	for(int i=1;i<(h/2)+1;i++){
		if(NthElement(head, i) == NthLastElement(head, i))
			result = 1;
		else{
			result = 0;
			break;
		}
	}
	return result;
		
}

void TestPalindrome(){
	struct Node* head = NULL;
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	AppendIteration(&head, 2);
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	return IsPalindrome(head);
}

int main(){
	TestPalindrome();
}


