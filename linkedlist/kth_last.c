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


//  print a linkedlist given the head node
void PrintLList(struct Node* node){
	while(node!=NULL){
		printf("%d ", node->data);
		node = node->next;
	}
}

//  Testing AppendIteration Method
struct Node* TestAppendIteration(){
	struct Node* head = NULL;
	int n = 1;
	while(n<=6){
 		AppendIteration(&head, n);
 		n+= 1;
	}
 	return head;
}

void FetchKthLastItem(struct Node* head, int k){
	struct Node* ref = head;
	struct Node* main = head;
	int i=1;
	if(k==0 || head==NULL){
		printf("cannot print k: %dth element\n", k);
		return;
	}
	while(i<k && ref->next!=NULL) {
		ref = ref->next;
		i = i+1;
	}
	if(i < k){
		printf("linkedlist has less elements than %d\n", k);
		return;
	}
	else if(ref->next == NULL){
		printf("%d\n", head->data);
		return;
	}
	while(main!=NULL && ref->next !=NULL){
		main = main->next;
		ref = ref->next;
	}
	printf("%d\n", main->data);
	return;

}



void PrintNthFromLast(struct Node* head, int k ){
	struct Node* ref = head;
	struct Node* main = head;
	int count = 0;
	if(head !=NULL && k != 0){
		while(count<k){
			if(ref == NULL){
				printf("%d is greater than the number of elements\n", k);
				return;
			}
			ref = ref->next;
			count = count+1;
		}
		while(ref!=NULL){
			main=main->next;
			ref = ref->next;
		}
		printf("Node no: %d from last is %d \n", k, main->data);
		return;
	}
	else{
		printf("Cannot print %dth node from the last\n", k);
		return;
	}
}

int main(){
	int k = 3;
	struct Node* head = TestAppendIteration();
	PrintLList(head);
	printf("\n");
	FetchKthLastItem(head, 1);
	FetchKthLastItem(head, 2);
	FetchKthLastItem(head, 3);
	FetchKthLastItem(head, 4);
	FetchKthLastItem(head, 5);
	FetchKthLastItem(head, 6);
	FetchKthLastItem(head, 7);
	FetchKthLastItem(head, 8);
	FetchKthLastItem(head, 0);

	PrintNthFromLast(head, 1);
	PrintNthFromLast(head, 2);
	PrintNthFromLast(head, 3);
	PrintNthFromLast(head, 4);
	PrintNthFromLast(head, 5);
	PrintNthFromLast(head, 6);
	PrintNthFromLast(head, 7);
	PrintNthFromLast(head, 8);
	PrintNthFromLast(head, 0);
}