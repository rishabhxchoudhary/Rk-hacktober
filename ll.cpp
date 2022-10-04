#include <iostream>

using namespace std;
class node{
public:
    int data;
    node *next;
    node(int d){
        data=d;
        next=NULL;
    }
};


int LengthLL(node*head){
    int ans=0;
    while(head!=NULL){
        head=head->next;
        ans++;
    }
    return ans;
}


void InsertAtFront(node*&head, node*&tail, int data){
    if(head==NULL){
        node*n = new node(data);
        head=tail=n;
    }
    else{
        node*n=new node(data);
        n->next=head;
        head=n;
    }
}


void InsertAtEnd(node* &head, node* &tail, int data){
    if(head==NULL){
        head=tail=new node(data);
    }
    else{
        node *n=new node (data);
        tail->next=n;
        tail=n;
    }
}


void InsertAtMid(node* &head, node* &tail, int pos, int data){
    if(pos==0){
        InsertAtFront(head, tail, data);
    }
    else if(pos>=LengthLL(head)){
        InsertAtEnd(head, tail, data);
    }
    else{
        node* temp=head;
        for(int i=1; i<=pos-1; i++){
            temp=temp->next;

        }
        node* n=new node(data);
        n->next=temp->next;
        temp->next=n;
        n->data=data;
    }
}


void DeleteAtFront(node* &head, node* &tail){
    if(head=NULL){
        return;
    }
    else if(head->next==NULL){
        delete head;
        head=tail=NULL;
    }
    else{
        node*t=head;
        head=head->next;
        delete t;
    }
}


void DeleteAtEnd(node*&head, node*&tail){
    if(head==NULL){
        return;
    }
    else if(head->next==NULL){
        delete head;
        head=tail=NULL;
    }
    else{
        node* temp=head;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        delete tail;
        temp->next=NULL;
        tail=temp;
    }
}


void DeleteAtMid(node*&head, node*&tail, int pos){
    if(head=NULL){
        return;
    }
    else if(head->next==NULL){
        delete head;
        head=tail=NULL;
    }
    else{
        node*temp=head;
        for(int i=1; i<=pos-1; i++){
            temp=temp->next;
        }
        node*n=temp->next;
        temp->next=n->next;
        delete n;
    }
}


void reverseLL(node*&head, node*&tail){
    node*c=head;
    node*p=NULL;
    while(c!=NULL){
        node*n=c->next;
        c->next=p;
        p=c;
        c=n;
    }
    swap(head,tail);
}


void reverseRecusionLLhelper(node*c, node*p){
    if(c==NULL){
        return;
    }
    node* n=c->next;
    c->next=p;
    reverseRecusionLLhelper(n,c);
}
void reverseRecusionLL(node*&head, node*&tail){
    reverseRecusionLLhelper(head,NULL);
    swap(head,tail);
}


node* mergeSortedLL(node*&h1, node*&h2){
    node*nh=NULL;
    if(h1->data>h2->data){
        nh=h2;
        return nh;
        nh->next=mergeSortedLL(h1, h2->next);
    }
    else if(h1->data<h2->data){
        nh=h1;
        return nh;
        nh->next=mergeSortedLL(h1->next, h2);
    }
}

node* findMid(node*head){
    if(head==NULL || head->next==NULL){
        return head;
    }
    node*slow=head;
    node*fast=head->next;
    while(fast and fast->next){
        fast=fast->next->next;
        slow=slow->next;
    }
    return slow;
}


void printLL(node* head){
    while(head!=NULL){
        cout<<head->data<<"-->";
        head=head->next;
    }
    cout<<"NULL\n";
}


int main()
{
    node *head=NULL, *tail=NULL;
    InsertAtFront(head, tail, 1);
    InsertAtFront(head, tail, 2);
    InsertAtFront(head, tail, 3);
    InsertAtFront(head, tail, 4);
    InsertAtFront(head, tail, 5);
    InsertAtEnd(head, tail, 0);
    InsertAtMid(head,tail, 3, 6);
    printLL(head);
    reverseLL(head, tail);
    printLL(head);
    cout<<findMid(head)->data;
    return 0;
}
