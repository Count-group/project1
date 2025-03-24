#include <iostream>
using namespace std;

// 定义链表节点
struct Node {
    int val;      // 存储的数值
    Node *next;   // 指向下一个节点的指针
    Node(int v) : val(v), next(nullptr) {}
};

// 定义队列类
class Queue {
private:
    Node *head;   // 队首指针
    Node *tail;   // 队尾指针
    int count;    // 队列中元素个数
public:
    Queue() : head(nullptr), tail(nullptr), count(0) {}

    // 析构函数，释放所有节点的内存
    ~Queue() {
        while (head != nullptr) {
            Node* tmp = head;
            head = head->next;
            delete tmp;
        }
    }

    // push(x)：将元素 x 加入队列尾部
    void push(int x) {
        Node* newNode = new Node(x);
        if (head == nullptr) {  // 队列为空时，头尾均指向新节点
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }

    // pop()：弹出队首元素，如果队列为空返回 false
    bool pop() {
        if (head == nullptr) {
            return false;
        }
        Node* tmp = head;
        head = head->next;
        if (head == nullptr) { // 弹出后队列为空，则更新 tail
            tail = nullptr;
        }
        delete tmp;
        count--;
        return true;
    }

    // front()：返回队首元素值（前提是队列非空）
    int front() {
        return head->val;
    }

    // size()：返回队列中元素个数
    int size() {
        return count;
    }

    // isEmpty()：判断队列是否为空
    bool isEmpty() {
        return head == nullptr;
    }
};

int main() {
    int n;
    cin >> n;
    Queue queue;

    // 依次处理 n 次操作
    for (int i = 0; i < n; i++) {
        int op;
        cin >> op;
        if (op == 1) {  // push 操作
            int x;
            cin >> x;
            // 题目保证 x 在 [1,1000000] 范围内
            queue.push(x);
        } else if (op == 2) { // pop 操作
            if (!queue.pop()) {
                cout << "ERR_CANNOT_POP" << "\n";  // 弹出失败，输出错误信息并空一行
            }
        } else if (op == 3) { // query 操作
            if (queue.isEmpty()) {
                cout << "ERR_CANNOT_QUERY" << "\n";  // 队列为空，输出错误信息并空一行
            } else {
                cout << queue.front() << "\n";        // 输出队首元素并空一行
            }
        } else if (op == 4) { // size 操作
            cout << queue.size() << "\n";             // 输出队列中元素个数并空一行
        }
    }
    return 0;
}
