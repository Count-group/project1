#include <iostream>
using namespace std;

struct Node {
    int val;
    Node* next;
    Node(int x) : val(x), next(nullptr) {}
};

class MyQueue {
private:
    Node* head;
    Node* tail;
    int count;

public:
    MyQueue() : head(nullptr), tail(nullptr), count(0) {}

    ~MyQueue() {
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    void push(int x) {
        Node* newNode = new Node(x);
        if (count == 0) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }

    void pop() {
        if (count == 0) {
            cout << "ERR_CANNOT_POP" << endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        delete temp;
        count--;
        if (count == 0) {
            tail = nullptr;
        }
    }

    void query() {
        if (count == 0) {
            cout << "ERR_CANNOT_QUERY" << endl;
        } else {
            cout << head->val << endl;
        }
    }

    void size() {
        cout << count << endl;
    }
};

int main() {
    MyQueue q;
    int n;
    cin >> n;
    int cmd;
    for (int i = 0; i < n; ++i) {
        cin >> cmd;
        if (cmd == 1) {
            int x;
            cin >> x;
            q.push(x);
        } else if (cmd == 2) {
            q.pop();
        } else if (cmd == 3) {
            q.query();
        } else if (cmd == 4) {
            q.size();
        }
    }
    return 0;
}