#include <iostream>
using namespace std;

struct Node {
    unsigned long long val;
    Node* next;
    Node(unsigned long long x) : val(x), next(nullptr) {}
};

class Stack {
private:
    Node* top;
    int count;

public:
    Stack() : top(nullptr), count(0) {}

    void push(unsigned long long x) {
        Node* newNode = new Node(x);
        newNode->next = top;
        top = newNode;
        count++;
    }

    void pop() {
        if (count == 0) {
            cout << "Empty" << endl;
            return;
        }
        Node* temp = top;
        top = top->next;
        delete temp;
        count--;
    }

    void query() {
        if (count == 0) {
            cout << "Anguei!" << endl;
        } else {
            cout << top->val << endl;
        }
    }

    void size() {
        cout << count << endl;
    }
};

int main() {
    string op;
    int T;
    cin>>T;
    while(T>0){
        int n;
        cin>>n;
        Stack stk;
        while (n>0) {
            cin>>op;
            if (op == "push") {
                unsigned long long x;
                cin >> x;
                stk.push(x);
            } else if (op == "pop") {
                stk.pop();
            } else if (op == "query") {
                stk.query();
            } else if (op == "size") {
                stk.size();
            }
            n--;
        }
        T--;
    }
    return 0;
}