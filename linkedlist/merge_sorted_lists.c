#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node* next;
};

struct Node* NewNode(int data){
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->data =data;
	new_node->next = NULL;
	return new_node;
}


struct Node* MergeLists(struct Node* head1, struct Node* head2){
	struct Node* result = NULL;
	if(head1 == NULL)
		return head2;
	if(head2 == NULL)
		return head1;
	if(head1->data <= head2->data){
		result = head1;
		result->next = MergeLists(head1->next, head2);
	}
	else{
		result = head2;
		result->next = MergeLists(head1, head2->next);
	}
	return result;

}
void PrintLL(struct Node* head){
	if(head == NULL)
		return;
	printf("%d ", head->data);
	PrintLL(head->next);
}



int main(){
	struct Node* head1 =  NULL;
	head1 = NewNode(1);
	head1->next = NewNode(6);
	head1->next->next = NewNode(9);

	struct Node* head2 = NULL;
	head2 = NewNode(2);
	head2->next = NewNode(3);
	head2->next->next = NewNode(5);
	head2->next->next->next = NewNode(8);

	struct Node* result = MergeLists(head1, head2);
	PrintLL(result);
}