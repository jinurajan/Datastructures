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
		find nth first and nth last element and compare until the length/2+1
		Complexity: 
			to find nth element: 1 iteration total n\2 for n/2 elements
			to find nth last element: 1 iteration total n/2 for n/2 elements
			height: one iteration
			n/2+n/2+n ~ 2n ~ O(n)
		Space Complexity:O(1); because we are not using extra space in memory
*/

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


/* 
	Method 2:
	Use a stack to store the values
	pop from stack and compare with current element if same proceed
	else break
	Time complexity: o(n)
	space complexity: o(n)
*/

// creating stack using linked list

struct Node* push(struct Node** top, int data){
	if(*(top)==NULL){
		*(top) = NewNode(data);
		return *top;
	}
	struct Node* temp = NewNode(data);
	temp->next = *(top);
	*(top) = temp;
	return *(top);
}

int pop(struct Node** top){
	if(top!=NULL){
		struct Node* temp = *(top);
		int result = temp->data;
		*top = temp->next;
		free(temp);
		return result;
	}
	else{
		printf("stack is empty\n");
		return 0;
	}
}

struct Node* CreateStack(struct Node* node){
	struct Node *top = NULL;
	while(node!=NULL){
		top = push(&top, node->data);
		node = node->next;
	}
	return top;
}



int IsPalindromeUsingStack(struct Node* head){
	// create stack which needs o(n) space and o(n) time
	struct Node* top = CreateStack(head);
	int is_palindrome = 0;
	while(head!=NULL){
		if(head->data != pop(&top)){
			is_palindrome = 0;
			return is_palindrome;
		}
		head= head->next;
		is_palindrome = 1;
	}
	return is_palindrome;
}


/* Method 3:
	Use Recursion to compare the left and right elements
	Using function stack as containers to store right and left element
	Time complexity: o(n)
	space complexity: o(n) if function stack considered else o(1)

*/

int IsPalindromeRecursion(struct Node** left, struct Node* right){
	if(right==NULL)
		return 1;
	int result = IsPalindromeRecursion(left, right->next);
	if(result == 0)
		return 0;
	int result_1 =0;
	if(right->data == (*left)->data)
		result_1 = 1;
	*left = (*left)->next;
	return result_1;
}


/* Method4: By reversing the list. find if the length of the list is odd or even 
find the middle node and reverse the second half and compare with the first one
 */

void reverse(struct Node** head){
	struct Node* prev = NULL;
	struct Node* current = *head;
	struct Node* next;
	while(current !=NULL){
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*(head) = prev;
}


int CompareLists(struct Node* head1, struct Node* head2){
	struct Node* temp1 = head1;
	struct Node* temp2 = head2;
	while(temp1 && temp2){
		if(temp1->data == temp2->data){
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return 0;
		if(temp1==NULL && temp2==NULL)
			return 1;
		return 0;
	}
	return 1;
}

int IsPalindromeReverse(struct Node* head){
	struct Node* fast_ptr=head, *slow_ptr = head;
	struct Node* midnode=NULL;
	struct Node* second_half, *prev_slow_ptr = head;
	int res=1;
	if(head!=NULL && head->next !=NULL){
		while(fast_ptr!=NULL & fast_ptr->next !=NULL){
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if(fast_ptr !=NULL){
			midnode = slow_ptr;
			slow_ptr= slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;
		reverse(&second_half);
		res = CompareLists(head, second_half);
		// rebuild the linkedlist
		reverse(&second_half);
		// midnode->next = second_half;
		if(midnode != NULL){
			prev_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_slow_ptr->next = second_half;
	}
	return res;
}


void is_odd_length(struct Node* head){
	struct Node* fast_ptr = head;
	struct Node* slow_ptr = head;
	struct Node* middle_ptr = head;
	while(fast_ptr !=NULL && fast_ptr->next != NULL){
		fast_ptr = fast_ptr->next->next;
		middle_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	// printf("fast_ptr: %d \n",fast_ptr->data);
	// printf("middle_ptr: %d\n", middle_ptr->data);
	// printf("slow_ptr%d\n", slow_ptr->data);
	if(fast_ptr == NULL){
		printf("\neven\n");
	}
	else
		printf("\nodd\n");
}


void TestIsPalindromeReverse(struct Node* head){
	if(IsPalindromeReverse(head))
		printf("IsPalindromeReverse says its palindrome\n");
	else
		printf("IsPalindromeReverse says its not a palindrome\n");
}



void TestIsPalindromeRecursion(struct Node* head){
	if(IsPalindromeRecursion(&head, head))
		printf("IsPalindromeRecursion says its palindrome\n");
	else
		printf("IsPalindromeRecursion says its not a palindrome\n");
}


void TestPalindromeUsingStack(struct Node* head){
	if(IsPalindromeUsingStack(head))
		printf("IsPalindromeUsingStack says its palindrome\n");
	else
		printf("IsPalindromeUsingStack says its not a palindrome\n");
}



void TestPalindrome(struct Node* head){
	if(IsPalindrome(head))
		printf("IsPalindrome says its palindrome\n");
	else
		printf("IsPalindrome says its not a palindrome\n");
}



int main(){
	struct Node* head = NULL;
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	AppendIteration(&head, 2);
	AppendIteration(&head, 1);
	AppendIteration(&head, 1);
	TestPalindrome(head);
	TestPalindromeUsingStack(head);
	TestIsPalindromeRecursion(head);
	TestIsPalindromeReverse(head);
}


