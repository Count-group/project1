#include <iostream>
#include <cstring>  // 用于 strcmp
using namespace std;

// 定义链表节点，每个节点存储一个 unsigned long long 数据
struct Node {
    unsigned long long data;
    Node *next;
};

// 自定义栈类，不依赖 STL 内置库
class Stack {
private:
    Node *top;   // 指向栈顶
    int cnt;     // 记录栈中元素个数
public:
    // 构造函数，初始化为空栈
    Stack(): top(nullptr), cnt(0) {}

    // 析构函数，释放所有节点
    ~Stack() {
        while(top != nullptr) {
            Node *temp = top;
            top = top->next;
            delete temp;
        }
    }

    // push(x)：向栈中加入一个数 x
    void push(unsigned long long x) {
        Node *newNode = new Node();
        newNode->data = x;
        newNode->next = top;
        top = newNode;
        cnt++;
    }

    // pop()：弹出栈顶元素，若栈为空则输出 "Empty"
    void pop() {
        if(top == nullptr) {
            cout << "Empty" << "\n";
        } else {
            Node *temp = top;
            top = top->next;
            delete temp;
            cnt--;
        }
    }

    // query()：输出栈顶元素，若栈为空则输出 "Anguei!"
    void query() {
        if(top == nullptr) {
            cout << "Anguei!" << "\n";
        } else {
            cout << top->data << "\n";
        }
    }

    // size()：输出当前栈内元素个数
    void size() {
        cout << cnt << "\n";
    }
};

int main() {
    // 使用快速 I/O，防止大数据量下吃土
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        int n;
        cin >> n;
        Stack s; // 每组数据单独使用一个栈
        while(n--) {
            char op[10];
            cin >> op;
            if(strcmp(op, "push") == 0) {
                unsigned long long x;
                cin >> x;
                s.push(x);
            } else if(strcmp(op, "pop") == 0) {
                s.pop();
            } else if(strcmp(op, "query") == 0) {
                s.query();
            } else if(strcmp(op, "size") == 0) {
                s.size();
            }
        }
    }
    return 0;
}
