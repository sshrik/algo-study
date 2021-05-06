#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define RED 0
#define BLACK 1

typedef struct _node {
    struct _node* parent;
    struct _node* left;
    struct _node* right;
    int value;
    int color;
}Node;

void printTree(Node* root);
void printNode(Node* root);
void addLeft(Node* root, Node* add);
void addRight(Node* root, Node* add);
void leftRotate(Node * root);
void rightRotate(Node * root);
Node* insert(Node* root, int value);
void fixup(Node* root, Node* newNode);
Node* getBrother(Node* root);
void delete(Node* root, Node* deleteNode);
Node* search(Node* root, int value);
Node* findRoot(Node* node);

int main() {
    Node* node[200];
    Node* root;
    int nodeIndex = 0;
    for(int i = 0; i < 200; i++) node[i] = NULL;
    node[nodeIndex] = insert(node[0], 41);  nodeIndex++;    root = findRoot(node[0]);
    node[nodeIndex] = insert(root, 38);  nodeIndex++;    root = findRoot(root);
    printf("\n");
    printTree(root);
    node[nodeIndex] = insert(root, 31);  nodeIndex++;    root = findRoot(root);
    printf("\n");
    printTree(root);
    node[nodeIndex] = insert(root, 12);  nodeIndex++;    root = findRoot(root);
    printf("\n");
    printTree(root);
    node[nodeIndex] = insert(root, 19);  nodeIndex++;    root = findRoot(root);
    printf("\n");
    printTree(root);
    node[nodeIndex] = insert(root, 8);   nodeIndex++;    root = findRoot(root);
    printf("\n");
    printTree(root);


    for(int i = 0; i < nodeIndex; i++) {
        free(node[i]);
    }
    return 0;
}

void printTree(Node* root) {
    if(root != NULL) {
        printNode(root);
        printTree(root->left);
        printTree(root->right);
    }
}

void printNode(Node* root) {
    if(root->color == RED) printf("\x1b[31mROOT : [%03d] \x1b[0m", root->value);
    else printf("\x1b[37mROOT : [%03d] \x1b[0m", root->value);
    if(root->left == NULL) {
        if(root->right == NULL) {
            if(root->parent == NULL) {
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", 0, 0, 0);
            }
            else {
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", 0, 0, root->parent->value);
            }
        }
        else {
            if(root->parent == NULL) { 
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", 0, root->right->value, 0);
            }
            else {
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n",0, root->right->value, root->parent->value);
            }
        }
    }
    else {
        if(root->right == NULL) {
            if(root->parent == NULL) { 
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", root->left->value, 0, 0);
            }
            else {
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", root->left->value, 0, root->parent->value);
            }
        }
        else{
            if(root->parent == NULL) { 
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", root->left->value, root->right->value, 0);
            }
            else {
                printf("LEFT : [%03d] RIGHT : [%03d] PARENT : [%03d]\n", root->left->value, root->right->value, root->parent->value);
            }
        }
    }
}

void addLeft(Node* root, Node* add) {
    root->left = add;
    add->parent = root;
}

void addRight(Node* root, Node* add) {
    root->right = add;
    add->parent = root;
}

void leftRotate(Node * root) {
    Node* x = root;
    Node* y = root->right;
    if(y->left == NULL) {
        x->right = NULL;
    }
    else {
        x->right = y->left;
        y->left->parent = x;
    }
    y->parent = x->parent;
    if(x->parent != NULL) {
        if(x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
    }
    else {
        y->parent = NULL;
        x->parent = y;
    }
    y->left = x;
    x->parent = y;
}

void rightRotate(Node * root) {
    Node* y = root;
    Node* x = root->left;
    if(x->right == NULL) {
        y->left = NULL;
    }
    else {
        y->left = x->right;
        x->right->parent = y;
    }
    x->parent = y->parent;
    if(y->parent != NULL) {
        if(y == y->parent->left) y->parent->left = x;
        else y->parent->right = x;
    }
    else {
        x->parent = NULL;
        y->parent = x;
    }
    x->right = y;
    y->parent = x;
}

Node* insert(Node* root, int value) {
    Node* temp, *next = root;
    temp = (Node *)malloc(sizeof(Node));
    temp->value = value;
    temp->parent = NULL;
    temp->left = NULL;
    temp->right = NULL;
    temp->color = RED;

    if(root == NULL) {
        root = temp;
        root->color = BLACK;
        return temp;
    }

    while(1) {
        if(next->value >= value) {
            if(next->left == NULL) {
                next->left = temp;
                temp->parent = next;
                break;
            }
            else next = next->left;
        }
        else if(next->value < value) {
            if(next->right == NULL) {
                next->right = temp;
                temp->parent = next;
                break;
            }
            else next = next->right;
        }
    }

    if(temp->parent->color == RED) fixup(root, temp);
    return temp;
}

void fixup(Node* root, Node* newNode) {
    Node *temp, *parent = newNode->parent;
    if(parent == NULL) {
        if(root->color == RED) root->color = BLACK;
        return;
    }
    if(parent->parent == NULL) {
        if(parent->color == RED) parent->color = BLACK;
        return;
    }

    Node* parentBrother = getBrother(parent);

    if(parent == parent->parent->left) {
        if(parentBrother == NULL) {
            if(newNode == parent->right) {
                leftRotate(parent);
                temp = parent;
                parent = newNode;
                newNode = temp;
            }
            Node* gp = newNode->parent->parent;
            rightRotate(gp);
            parent->color = BLACK;
            gp->color = RED;

        }
        else if(parentBrother->color == BLACK) {
            if(newNode == parent->right) {
                leftRotate(parent);
                temp = parent;
                parent = newNode;
                newNode = temp;
            }
            Node* gp = newNode->parent->parent;
            rightRotate(gp);
            parent->color = BLACK;
            gp->color = RED;
        }
        else {
            parent->color = BLACK;
            parentBrother->color = BLACK;
            parent->parent->color = RED;
            fixup(root, parent->parent);
        }
    }
    else {
        if(parentBrother == NULL) {
            if(newNode == parent->left) {
                rightRotate(parent);
                temp = parent;
                parent = newNode;
                newNode = temp;
            }
            Node* gp = newNode->parent->parent;
            leftRotate(gp);
            parent->color = BLACK;
            gp->color = RED;
        }
        else if(parentBrother->color == BLACK) {
            if(newNode == parent->left) {
                rightRotate(parent);
                temp = parent;
                parent = newNode;
                newNode = temp;
            }
            Node* gp = newNode->parent->parent;
            leftRotate(gp);
            parent->color = BLACK;
            gp->color = RED;
        }
        else {
            parent->color = BLACK;
            parentBrother->color = BLACK;
            parent->parent->color = RED;
            fixup(root, parent->parent);
        }
    }
}

Node* getBrother(Node* root) {
    Node* parent = root->parent;
    if(parent->left == root) return parent->right;
    else return parent->left;
}


void delete(Node* root, Node* deleteNode) {

}

Node* search(Node* root, int value) {
    if(root->value < value) return search(root->right, value);
    else if(root->value > value) return search(root->left, value);
    else return root;
}
Node* findRoot(Node* node) {
    if(node->parent == NULL) return node;
    else return findRoot(node->parent);
}