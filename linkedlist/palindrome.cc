// Author: Jinu.P.R
// Date: Dec 22 2016
// Copyright: Always restricted to those who know what linkedlist is and how does it work ;)
// http://www.practice.geeksforgeeks.org/problem-page.php?pid=700391

#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace std;
/* Link list Node */
struct Node
{
    int data;
    struct Node* next;
};

void append(struct Node** head_ref, struct Node **tail_ref, int new_data)
{
    struct Node* new_node = new Node;
    new_node->data  = new_data;
    new_node->next = NULL;
    if (*head_ref == NULL)
       *head_ref = new_node;
    else
       (*tail_ref)->next = new_node;
    *tail_ref = new_node;
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

bool isPalindrome(struct Node* head){
	int h = height(head);
	if(h==0){
		printf("LL is empty\n");
		return 0;
	}
	if(h==1){
		return 1;
	}
	bool result = false;
	for(int i=1;i<(h/2)+1;i++){
		if(NthElement(head, i) == NthLastElement(head, i))
			result = true;
		else{
			result = false;
			break;
		}
	}
	return result;
		
}


// bool isPalindrome(Node *head);
/* Driver program to test above function*/
int main()
{
  int T,i,n,l;
    cin>>T;
    while(T--){
    struct Node *head = NULL,  *tail = NULL;
        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>l;
            append(&head, &tail, l);
        }
   	cout<<isPalindrome(head)<<endl;
    }
    return 0;
}




