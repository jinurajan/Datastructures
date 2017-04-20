/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node;

Node* NewNode(int data){
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}


int GetCount(Node* node){
    if(node == NULL)
        return 0;
    else
        return 1+GetCount(node->next);
}

int FindMergeNodeUtil(int d, Node* head1, Node* head2){
    //head1 is always bigger
    int i =0;
    Node* temp1 = head1;
    Node* temp2 = head2;
    while(i < d){
        temp1 = temp1->next;
        i+=1;
    }
    // now the lengths are equal for both list
    while(temp1 != NULL && temp2 != NULL){
        if(temp1 == temp2)
            return temp1->data;
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    return -1;
}

int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method. 
    int c1 = GetCount(headA);
    int c2 = GetCount(headB);
    int d;
    if(c1 > c2){
        d = c1-c2;
        return FindMergeNodeUtil(d, headA, headB);
    }
    else{
        d = c2-c1;
        return FindMergeNodeUtil(d, headB, headA);
    }
    return -1;
}

int main(){
    Node* head1 = NULL;
    Node* head2 = NULL;
    head1 = NewNode(2);
    head1->next = NewNode(3);
    head1->next->next = NewNode(4);
    head1->next->next->next = NewNode(5);

    head2 = NewNode(6);
    head2->next = head1->next;
    head2->next->next = NewNode(7);

    printf("%d\n",FindMergeNode(head1, head2));
}
