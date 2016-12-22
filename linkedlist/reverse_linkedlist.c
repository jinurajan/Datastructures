#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node* next;
};

struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data = data;
	new_node->next = NULL;
	return new_node;
};

void insert(struct Node** head, int data){
	struct Node* new_node = NewNode(data);
	if(*(head) == NULL){
		*(head) = new_node;
		return;
	}

	struct Node* temp = *head;
	while(temp->next != NULL){
		temp = temp->next;
	}
	temp->next = new_node;
	return;
}

void ReverseIteration(struct Node** head){
	struct Node* prev = NULL;
	struct Node* current = *(head);
	struct Node* next;
	while(current !=NULL){
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*(head) = prev;

}

void ReverseRecursion(struct Node** head){
	struct Node* first;
	struct Node* rest;
	if(*(head) == NULL)
		return;
	first = *(head);
	rest = first->next;
	if(rest == NULL)
		return;
	ReverseRecursion(&rest);
	first->next->next = first;
	first->next = NULL;
	*(head) = rest;
}


void ReverseRecursionwithHead(struct Node* current, struct Node* prev, struct Node** head){
	if(current->next == NULL){
		*(head) = current;
		current->next = prev;
		return;
	}
	struct Node* next = current->next;
	current->next = prev;
	ReverseRecursionwithHead(next, current, head);
}


void PrintLL(struct Node* head){
	while(head !=NULL){
		printf("%d ", head->data);
		head = head->next;
	}
}


void TestReverseRecursionMethod2(){
	int i = 1;
	printf("\nTesting Recursion Method2 using head pointer\n");
	struct Node* head1 = NULL;

	while(i<6){
		insert(&head1, i);
		i=i+1;
	}
	PrintLL(head1);
	printf("\n");
	ReverseRecursionwithHead(head1, NULL, &head1);
	PrintLL(head1);
}




void TestReverseRecursion(){
	int i = 1;
	printf("\nTesting Recursion\n");
	struct Node* head1 = NULL;

	while(i<6){
		insert(&head1, i);
		i=i+1;
	}
	PrintLL(head1);
	printf("\n");
	ReverseRecursion(&head1);
	PrintLL(head1);
}


int main(){
	int i =1;
	printf("\nTesting Reverse Iteration\n");
	struct Node* head = NULL;
	while(i<6){
		insert(&head, i);
		i=i+1;
	}
	
	PrintLL(head);
	printf("\n");
	ReverseIteration(&head);
	PrintLL(head);
	TestReverseRecursion();
	TestReverseRecursionMethod2();
}